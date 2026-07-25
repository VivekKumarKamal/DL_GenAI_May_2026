import os
import json
import time
import requests
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# Dynamic path resolution so the pipeline runs portably on any machine/environment
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Input CSV: manually checked queue file
QUEUE_PATH = os.path.join(BASE_DIR, "topics_to_fetch_manually_checked.csv")

CACHE_DIR = os.path.join(BASE_DIR, "wiki_corpus")
FAILURES_LOG_PATH = os.path.join(BASE_DIR, "fetch_failures.json")

# Wikipedia API Configuration
WIKI_API_URL = "https://en.wikipedia.org/w/api.php"
HEADERS = {
    "User-Agent": "SmartMCQSolverBot/1.0 (https://github.com/example/mcq-solver; contact: student@example.com)"
}
MAX_WORKERS = 2        # 2 worker threads + polite delays to respect Wikipedia API rate limits (avoid HTTP 429)
MAX_RETRIES = 5        # Retries per request with exponential backoff
DELAY_BETWEEN_REQ = 0.25  # Delay in seconds between API requests
TOP_K_ARTICLES = 2    # Download top 2 articles per topic search for broader RAG context coverage


def make_wikipedia_api_request(params: dict, session: requests.Session) -> dict | None:
    """
    Helper function to perform Wikipedia API GET requests with robust HTTP 429 rate-limit handling,
    exponential backoff, and safe JSON parsing.
    """
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(WIKI_API_URL, params=params, headers=HEADERS, timeout=12)
            
            # Rate limit hit (HTTP 429) -> wait and retry with exponential backoff
            if resp.status_code == 429:
                wait_time = int(resp.headers.get("Retry-After", attempt * 2))
                time.sleep(wait_time)
                continue
                
            if resp.status_code == 200:
                return resp.json()
                
        except (requests.RequestException, ValueError, json.JSONDecodeError):
            time.sleep(attempt * 1.5)
            
        time.sleep(DELAY_BETWEEN_REQ)
        
    return None


def search_wikipedia_titles(topic: str, session: requests.Session, top_k: int = TOP_K_ARTICLES) -> list[str]:
    """
    Query Wikipedia's Search API to find the top `top_k` canonical article titles for a topic string.
    This resolves descriptive topics to their most relevant Wikipedia articles (e.g. top 2 results).
    """
    params = {
        "action": "query",
        "list": "search",
        "srsearch": topic,
        "format": "json",
        "srlimit": top_k,
    }
    data = make_wikipedia_api_request(params, session)
    titles = []
    if data:
        results = data.get("query", {}).get("search", [])
        for item in results:
            if "title" in item:
                titles.append(item["title"])
    return titles


def fetch_wikipedia_text(title: str, session: requests.Session) -> str | None:
    """
    Fetch the full plain-text extract of a Wikipedia page using MediaWiki prop=extracts.
    Follows redirects automatically (explaintext=True returns clean markdown-friendly text).
    """
    params = {
        "action": "query",
        "prop": "extracts",
        "explaintext": True,
        "titles": title,
        "redirects": 1,
        "format": "json",
    }
    data = make_wikipedia_api_request(params, session)
    if data:
        pages = data.get("query", {}).get("pages", {})
        for page_id, page_info in pages.items():
            if page_id != "-1" and "extract" in page_info:
                return page_info["extract"]
    return None


def fetch_and_save_topic(row: dict, session: requests.Session) -> dict:
    """
    Process a single topic row: search Wikipedia for the top 2 articles, retrieve page texts,
    and save them as separate Markdown files (e.g., 'topic.md' for Rank #1 and 'topic_2.md' for Rank #2).
    """
    topic = row["topic"]
    filename = row["cache_filename"]
    base_name, ext = os.path.splitext(filename)

    # Determine file paths for Top 2 articles
    # Rank 1: 'einstein.md'
    # Rank 2: 'einstein_2.md'
    file_1 = os.path.join(CACHE_DIR, filename)
    file_2 = os.path.join(CACHE_DIR, f"{base_name}_2{ext}")

    # Check if both articles are already downloaded and valid (>100 bytes)
    has_1 = os.path.exists(file_1) and os.path.getsize(file_1) > 100
    has_2 = os.path.exists(file_2) and os.path.getsize(file_2) > 100

    if has_1 and has_2:
        return {"topic": topic, "status": "already_cached", "filename": filename, "articles_saved": 2}

    time.sleep(DELAY_BETWEEN_REQ)

    # 1. Search Wikipedia API for top 2 titles
    wiki_titles = search_wikipedia_titles(topic, session, top_k=TOP_K_ARTICLES)
    if not wiki_titles:
        return {"topic": topic, "status": "search_failed", "filename": filename, "error": "No Wikipedia search match found"}

    example_id = row.get("example_row_id", "N/A")
    source = row.get("source", "N/A")
    freq = row.get("frequency", 1)

    saved_count = 0
    saved_titles = []

    # 2. Iterate through returned search results (up to top 2)
    for rank, wiki_title in enumerate(wiki_titles, start=1):
        target_filepath = file_1 if rank == 1 else file_2

        # Skip if this specific rank file is already cached
        if os.path.exists(target_filepath) and os.path.getsize(target_filepath) > 100:
            saved_count += 1
            saved_titles.append(wiki_title)
            continue

        time.sleep(DELAY_BETWEEN_REQ)

        # Retrieve full article text
        content = fetch_wikipedia_text(wiki_title, session)
        if content and len(content.strip()) >= 100:
            markdown_doc = f"""# {wiki_title}

> **Query Topic**: {topic} (Rank #{rank} Search Result)  
> **Source Queue**: {source} (Row ID: {example_id}, Frequency: {freq})  
> **Wikipedia Page**: https://en.wikipedia.org/wiki/{wiki_title.replace(' ', '_')}

---

{content.strip()}
"""
            with open(target_filepath, "w", encoding="utf-8") as f:
                f.write(markdown_doc)

            saved_count += 1
            saved_titles.append(wiki_title)

    if saved_count == 0:
        return {"topic": topic, "status": "fetch_failed", "filename": filename, "error": "Empty or short article content for all results"}

    return {
        "topic": topic,
        "status": "success",
        "filename": filename,
        "saved_count": saved_count,
        "saved_titles": saved_titles,
    }


def main():
    # ---------------------------------------------------------------------------
    # Step 1: Load input queue file
    # ---------------------------------------------------------------------------
    if not os.path.exists(QUEUE_PATH):
        print(f"Error: Queue CSV file not found at {QUEUE_PATH}")
        return

    print(f"Using manually checked queue: {QUEUE_PATH}")
    queue_df = pd.read_csv(QUEUE_PATH)
    print(f"Loaded {len(queue_df)} topics to process (fetching Top {TOP_K_ARTICLES} Wikipedia articles per topic).")

    # ---------------------------------------------------------------------------
    # Step 2: Ensure cache directory exists
    # ---------------------------------------------------------------------------
    os.makedirs(CACHE_DIR, exist_ok=True)

    # Convert DataFrame records to list of dicts
    topic_records = queue_df.to_dict("records")

    already_cached = 0
    newly_fetched = 0
    failed = []

    # ---------------------------------------------------------------------------
    # Step 3: Concurrent Multi-Threaded Fetching
    # ---------------------------------------------------------------------------
    print(f"\nFetching Top {TOP_K_ARTICLES} Wikipedia articles using {MAX_WORKERS} rate-limited threads...")
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        with requests.Session() as session:
            # Submit tasks to thread pool
            future_to_row = {
                executor.submit(fetch_and_save_topic, row, session): row
                for row in topic_records
            }

            # Progress bar monitoring
            for future in tqdm(as_completed(future_to_row), total=len(topic_records), desc="Downloading Wiki Corpus"):
                res = future.result()
                status = res.get("status")

                if status == "already_cached":
                    already_cached += 1
                elif status == "success":
                    newly_fetched += 1
                else:
                    failed.append(res)

    # ---------------------------------------------------------------------------
    # Step 4: Print Summary Statistics
    # ---------------------------------------------------------------------------
    print("\n" + "=" * 50)
    print(" FETCH SUMMARY REPORT")
    print("=" * 50)
    print(f"Total topics in queue   : {len(topic_records)}")
    print(f"Already fully cached    : {already_cached} (skipped)")
    print(f"Newly downloaded topics : {newly_fetched}")
    print(f"Failed topics           : {len(failed)}")
    print(f"Wiki Corpus directory   : {CACHE_DIR}")

    if failed:
        with open(FAILURES_LOG_PATH, "w", encoding="utf-8") as f:
            json.dump(failed, f, indent=2)
        print(f"\n⚠️  Saved {len(failed)} failed topic details to: {FAILURES_LOG_PATH}")
        print("First 5 failed topics:")
        for fail in failed[:5]:
            print(f"  - {fail['topic']}: {fail.get('error')}")


if __name__ == "__main__":
    main()
