"""
Repair the mangled formulas in the fetched Wikipedia corpus.

Wikipedia's `prop=extracts&explaintext=1` API does not render math. It walks the
MathML tree and emits every leaf text node on its own indented line, so a single
equation explodes into hundreds of lines holding one symbol each:

        L
        (
        ϱ
        )
        =
                      1
                      2
                  tr

That debris is 19.8% of this corpus (4.9 MB across 302 of 771 files). It wrecks
retrieval three ways: it floods the TF-IDF vocabulary with single-character
"terms", it produces junk chunks that can out-rank real prose, and it burns
context budget when one of those chunks is retrieved.

This script does two things per file:

  1. Collapses each run of indented MathML lines back into one inline formula.
  2. Drops the trailing `{\\displaystyle ...}` copy. The extractor emits every
     formula twice -- once in compact Unicode, once as LaTeX -- and the LaTeX
     duplicate contributes only command tokens (\\frac, \\int, \\displaystyle)
     that match nothing a question would ever say.

DRY RUN BY DEFAULT -- nothing is written until you pass --apply.

    python fix_corpus_math.py                    # preview
    python fix_corpus_math.py --apply            # rewrite in place
    python fix_corpus_math.py --apply --keep-latex
    python fix_corpus_math.py --dir some_corpus
"""

import os
import re
import sys
import glob
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CORPUS = os.path.join(BASE_DIR, "wiki_corpus")

# The extractor indents MathML leaves; ordinary extract prose never is.
INDENTED = re.compile(r"^[ \t]{2,}\S")


def collapse_math_runs(text: str, keep_latex: bool = False) -> str:
    """Join runs of indented MathML leaf lines back into single-line formulas."""
    out, buf = [], []

    def flush():
        if not buf:
            return
        # Concatenate without separators: the leaves are already the formula's
        # tokens in order, so "tr" + "(" + "ρ" reads back as "tr(ρ".
        formula = "".join(buf).strip()
        if formula:
            out.append(formula if keep_latex else drop_latex_duplicate(formula))
        buf.clear()

    for line in text.split("\n"):
        if INDENTED.match(line):
            buf.append(line.strip())
        elif buf and not line.strip():
            # Blank lines inside a formula block are part of the debris.
            continue
        else:
            flush()
            out.append(line)
    flush()

    # The MathML blocks are riddled with whitespace-only lines that are not
    # indented, so they survive the collapse and leave the file 64% blank.
    # Squeeze any run of blank lines down to a single paragraph break.
    return re.sub(r"\n{3,}", "\n\n", "\n".join(l.rstrip() for l in out)).strip() + "\n"


def drop_latex_duplicate(line: str) -> str:
    """Remove the trailing '{\\displaystyle ...}' twin of a Unicode formula."""
    idx = line.find("{\\displaystyle")
    if idx == -1:
        return line
    head = line[:idx].strip()
    # If the Unicode half is missing, keep the LaTeX rather than losing the maths.
    return head if head else line


def debris_chars(text: str) -> int:
    return sum(len(l) + 1 for l in text.split("\n") if INDENTED.match(l))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=DEFAULT_CORPUS, help="corpus directory")
    ap.add_argument("--apply", action="store_true", help="rewrite files (default: dry run)")
    ap.add_argument("--keep-latex", action="store_true",
                    help="keep the {\\displaystyle ...} duplicate of each formula")
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(args.dir, "*.md")))
    if not files:
        sys.exit(f"ERROR: no .md files in {args.dir}")

    before_total = after_total = 0
    touched = []

    for path in files:
        raw = open(path, encoding="utf-8").read()
        cleaned = collapse_math_runs(raw, keep_latex=args.keep_latex)
        before_total += len(raw)
        after_total += len(cleaned)
        if cleaned != raw:
            touched.append((os.path.basename(path), len(raw), len(cleaned)))
            if args.apply:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(cleaned)

    saved = before_total - after_total
    print(f"Corpus directory : {args.dir}")
    print(f"Files            : {len(files)}")
    print(f"Files with math  : {len(touched)}")
    print(f"Chars before     : {before_total:,}")
    print(f"Chars after      : {after_total:,}")
    print(f"Removed          : {saved:,}  ({saved / max(before_total, 1):.1%})")
    print()

    touched.sort(key=lambda r: r[1] - r[2], reverse=True)
    print("Biggest reductions:")
    for name, b, a in touched[:10]:
        print(f"  {name[:52]:52s} {b:>9,} -> {a:>8,}  (-{(b - a) / b:.0%})")

    if not args.apply:
        print("\nDRY RUN — nothing written. Re-run with --apply to rewrite these files.")
    else:
        print(f"\nRewrote {len(touched)} files in place.")


if __name__ == "__main__":
    main()
