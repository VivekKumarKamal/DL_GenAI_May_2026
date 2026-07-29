"""
Rename every .md file in the wiki corpus to a Kaggle-safe filename.

Kaggle rejects dataset uploads whose filenames contain characters outside a
narrow ASCII set. Faithful Wikipedia titles routinely break that rule:

    Navier-Stokes_equations.md   en dash (U+2013)
    Bell's_theorem.md            apostrophe
    Schrodinger_equation.md      umlaut
    Mercury_(planet).md          parentheses

This script walks the corpus, works out the correct name for each file, and
renames it. The target name comes from the article title recorded in the file's
front matter (`# Title`), so files still carrying legacy topic-based names get
canonicalised at the same time. Files with no readable title fall back to
sanitising their existing filename.

It reuses `title_to_filename` from fetcher.py, so the naming rule has exactly one
definition and the two scripts can never drift apart.

DRY RUN BY DEFAULT — nothing is touched until you pass --apply.

    python fix_corpus_filenames.py                       # preview
    python fix_corpus_filenames.py --apply               # rename
    python fix_corpus_filenames.py --apply --dedupe      # rename + drop exact duplicates
    python fix_corpus_filenames.py --dir some_corpus     # non-default directory
"""

import os
import re
import sys
import json
import hashlib
import argparse

from fetcher import title_to_filename, normalize_title
from fetcher import _UNSAFE_FILENAME_CHARS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CORPUS = os.path.join(BASE_DIR, "wiki_corpus")


def read_article_title(path: str) -> str | None:
    """Pull the Wikipedia title out of the file's front matter."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            head = f.read(2048)
    except OSError:
        return None

    match = re.match(r"#\s+(.+)", head)
    if not match:
        match = re.search(r"\*\*Wikipedia Page\*\*:\s*\S+/wiki/(\S+)", head)
    if not match:
        return None
    return match.group(1).replace("_", " ").strip()


def is_kaggle_safe(filename: str) -> bool:
    stem, _ = os.path.splitext(filename)
    return not _UNSAFE_FILENAME_CHARS.search(stem)


def file_digest(path: str) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def plan_renames(corpus_dir: str):
    """Decide a target filename for every .md file. Returns (plan, duplicates)."""
    files = sorted(f for f in os.listdir(corpus_dir) if f.endswith(".md"))

    plan = []          # (current_name, target_name, reason)
    duplicates = []    # (current_name, keeps_name) — same article, redundant copy
    taken = {}         # target_name -> identity of the file that claimed it

    for name in files:
        path = os.path.join(corpus_dir, name)

        title = read_article_title(path)
        if title:
            target, reason = title_to_filename(title), "from article title"
            # The article title is the identity. Two files for the same article
            # are copies even when their bytes differ, because the fetcher stamps
            # a different "Query Topic" line into each one's front matter.
            identity = normalize_title(title)
        else:
            # No front matter — sanitise whatever the file is called, and fall
            # back to content hashing to spot copies.
            stem, ext = os.path.splitext(name)
            target, reason = title_to_filename(stem.replace("_", " ")), "sanitised filename"
            identity = file_digest(path)

        if target in taken:
            if taken[target] == identity:
                duplicates.append((name, target))       # same article, drop it
                continue
            # Same safe name, genuinely different article: disambiguate.
            stem, ext = os.path.splitext(target)
            suffix = hashlib.md5(identity.encode("utf-8")).hexdigest()[:6]
            target = f"{stem}_{suffix}{ext}"
            reason += " (+hash, name collision)"

        taken[target] = identity
        if target != name:
            plan.append((name, target, reason))

    return plan, duplicates


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=DEFAULT_CORPUS, help="corpus directory")
    ap.add_argument("--apply", action="store_true", help="actually rename (default: dry run)")
    ap.add_argument("--dedupe", action="store_true",
                    help="delete byte-identical duplicates instead of keeping them")
    args = ap.parse_args()

    corpus_dir = args.dir
    if not os.path.isdir(corpus_dir):
        sys.exit(f"ERROR: no such directory: {corpus_dir}")

    files = [f for f in os.listdir(corpus_dir) if f.endswith(".md")]
    unsafe_before = [f for f in files if not is_kaggle_safe(f)]

    print(f"Corpus directory : {corpus_dir}")
    print(f"Markdown files   : {len(files)}")
    print(f"Kaggle-unsafe    : {len(unsafe_before)}")
    print()

    plan, duplicates = plan_renames(corpus_dir)

    if not plan and not duplicates:
        print("Nothing to do — every filename is already correct.")
        return

    print(f"Renames planned  : {len(plan)}")
    print(f"Exact duplicates : {len(duplicates)}")
    print()

    for old, new, reason in plan[:25]:
        print(f"  {old}\n    -> {new}   [{reason}]")
    if len(plan) > 25:
        print(f"  ... and {len(plan) - 25} more")

    if duplicates:
        print("\nByte-identical duplicates "
              f"({'will be deleted' if args.dedupe else 'kept — pass --dedupe to remove'}):")
        for old, keeps in duplicates[:10]:
            print(f"  {old}  == {keeps}")
        if len(duplicates) > 10:
            print(f"  ... and {len(duplicates) - 10} more")

    if not args.apply:
        print("\nDRY RUN — nothing changed. Re-run with --apply to perform these renames.")
        return

    # ── Execute ──────────────────────────────────────────────────────────────
    # Two phases via temporary names, so a rename cycle (a -> b, b -> a) or a
    # rename onto a name still occupied by a not-yet-moved file cannot clobber.
    log, staged = [], []
    for i, (old, new, _) in enumerate(plan):
        tmp = os.path.join(corpus_dir, f".rename_tmp_{i}_{os.getpid()}")
        os.rename(os.path.join(corpus_dir, old), tmp)
        staged.append((tmp, new, old))

    for tmp, new, old in staged:
        dest = os.path.join(corpus_dir, new)
        os.rename(tmp, dest)
        log.append({"from": old, "to": new})

    removed = 0
    if args.dedupe:
        for old, _keeps in duplicates:
            path = os.path.join(corpus_dir, old)
            if os.path.exists(path):
                os.remove(path)
                removed += 1

    remaining = [f for f in os.listdir(corpus_dir) if f.endswith(".md")]
    still_unsafe = [f for f in remaining if not is_kaggle_safe(f)]

    # Log next to the corpus it describes, not next to this script.
    log_path = os.path.join(os.path.dirname(os.path.abspath(corpus_dir)), "rename_log.json")
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 55)
    print(" DONE")
    print("=" * 55)
    print(f"Renamed          : {len(log)}")
    print(f"Duplicates removed: {removed}")
    print(f"Files remaining  : {len(remaining)}")
    print(f"Still unsafe     : {len(still_unsafe)}")
    if still_unsafe:
        print("  " + ", ".join(still_unsafe[:5]))
    print(f"Rename log       : {log_path}")


if __name__ == "__main__":
    main()
