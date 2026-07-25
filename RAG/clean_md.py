"""
clean_and_chunk_corpus.py
===========================
Takes the raw .md files you fetched from Wikipedia's search API
(in wiki_corpus/) and turns them into a clean, deduped, chunked
Parquet corpus ready for retrieval.

Two problems this solves:
 1. Wikipedia markdown carries boilerplate (References, See Also,
    External Links, footnote markers, tables, image embeds, link syntax)
    that hurts retrieval quality if left in.
 2. Fetching top-2 articles per topic across ~297 topics likely pulled
    the SAME article in more than once under different topic queries --
    this dedupes by article title before chunking.

Run it with:  python3 clean_and_chunk_corpus.py
"""

import re
import os
import glob
import pandas as pd

RAW_MD_DIR = "wiki_corpus"
OUTPUT_PARQUET = "knowledge_corpus.parquet"

CHUNK_WORDS = 150
OVERLAP_WORDS = 30

# Section headers that mark the start of boilerplate we want to drop --
# everything from one of these headers to the end of the file is cut.
BOILERPLATE_HEADERS = [
    "see also", "references", "external links", "notes",
    "further reading", "bibliography", "citations",
]


# ---------------------------------------------------------------------------
# STEP 1: Extract the title from a raw markdown file
# ---------------------------------------------------------------------------
def extract_title(raw_text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", raw_text, flags=re.MULTILINE)
    if match:
        return match.group(1).strip()
    return fallback


# ---------------------------------------------------------------------------
# STEP 2: Cut off boilerplate sections (References, See Also, etc.)
# ---------------------------------------------------------------------------
def cut_boilerplate(raw_text: str) -> str:
    lines = raw_text.split("\n")
    cutoff = len(lines)
    for i, line in enumerate(lines):
        header_match = re.match(r"^#{1,3}\s+(.+)$", line.strip())
        if header_match:
            header_text = header_match.group(1).strip().lower()
            if header_text in BOILERPLATE_HEADERS:
                cutoff = i
                break
    return "\n".join(lines[:cutoff])


# ---------------------------------------------------------------------------
# STEP 3: Strip markdown syntax down to plain prose
# ---------------------------------------------------------------------------
def clean_markdown(text: str) -> str:
    # Drop image/file embeds entirely: [[File:...]] or ![alt](url)
    text = re.sub(r"\[\[File:.*?\]\]", "", text, flags=re.IGNORECASE)
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)

    # Drop table rows (lines starting with |, and separator rows like |---|---|)
    text = re.sub(r"^\|.*\|\s*$", "", text, flags=re.MULTILINE)

    # Convert markdown links [text](url) -> text
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)

    # Strip footnote markers like [1], [12], [1][2]
    text = re.sub(r"\[\d+\]", "", text)

    # Strip bold/italic markers
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)

    # Strip remaining markdown headers, keep the text as a plain line
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)

    # Strip bullet/list markers
    text = re.sub(r"^[\-\*]\s+", "", text, flags=re.MULTILINE)

    # Collapse all whitespace/newlines into single spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# ---------------------------------------------------------------------------
# STEP 4: Chunk into overlapping passages (same logic as before)
# ---------------------------------------------------------------------------
def chunk_text(text: str, chunk_words: int = CHUNK_WORDS, overlap_words: int = OVERLAP_WORDS):
    words = text.split(" ")
    if len(words) <= chunk_words:
        return [text] if text else []

    chunks = []
    start = 0
    step = chunk_words - overlap_words
    while start < len(words):
        chunk = words[start:start + chunk_words]
        chunks.append(" ".join(chunk))
        if start + chunk_words >= len(words):
            break
        start += step

    return chunks


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    md_files = sorted(glob.glob(os.path.join(RAW_MD_DIR, "*.md")))
    print(f"Found {len(md_files)} raw markdown files in {RAW_MD_DIR}/")

    if not md_files:
        print("No .md files found -- nothing to do. Check RAW_MD_DIR.")
        return

    seen_titles = set()   # for dedup (normalized, lowercase)
    articles = []          # list of (title, cleaned_text)
    skipped_dupes = 0
    skipped_empty = 0

    for path in md_files:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()

        fallback_title = os.path.splitext(os.path.basename(path))[0]
        title = extract_title(raw, fallback_title)
        title_key = title.strip().lower()

        if title_key in seen_titles:
            skipped_dupes += 1
            continue
        seen_titles.add(title_key)

        body = cut_boilerplate(raw)
        cleaned = clean_markdown(body)

        if len(cleaned.split()) < 20:  # too short to be useful, likely a stub/redirect
            skipped_empty += 1
            continue

        articles.append((title, cleaned))

    print(f"Skipped as duplicate articles : {skipped_dupes}")
    print(f"Skipped as too short/empty    : {skipped_empty}")
    print(f"Articles kept for chunking    : {len(articles)}")

    # ---- Chunk everything ----
    rows = []
    chunk_id = 0
    for title, cleaned in articles:
        chunks = chunk_text(cleaned)
        for i, chunk in enumerate(chunks):
            rows.append({
                "chunk_id": chunk_id,
                "article_title": title,
                "chunk_index_in_article": i,
                "text": chunk,
                "word_count": len(chunk.split(" ")),
            })
            chunk_id += 1

    corpus_df = pd.DataFrame(rows)
    print(f"\nTotal chunks produced: {len(corpus_df)}")
    if len(corpus_df):
        print(f"Avg words per chunk  : {corpus_df['word_count'].mean():.1f}")

    corpus_df.to_parquet(OUTPUT_PARQUET, index=False)
    print(f"\nSaved corpus to: {OUTPUT_PARQUET}")

    # sanity check: reload it
    reloaded = pd.read_parquet(OUTPUT_PARQUET)
    assert len(reloaded) == len(corpus_df), "Row count mismatch after reload!"
    print(f"Reloaded successfully: {len(reloaded)} rows confirmed.")

    if len(corpus_df):
        print("\nSample cleaned chunk (this is what the retriever will search over):")
        print(f'  "{corpus_df.iloc[0]["text"][:400]}..."')


if __name__ == "__main__":
    main()