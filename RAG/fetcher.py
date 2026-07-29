# It fetches the top 3 articles from searching topics_to_search
# renames file names so they don't contain any unallowed characters in kaggle

import os
import re
import sys
import json
import time
import hashlib
import threading
import unicodedata
import requests
from urllib.parse import quote
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEFAULT_QUEUE_PATH = os.path.join(BASE_DIR, "topics_to_fetch.csv")
QUEUE_PATH = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_QUEUE_PATH

CACHE_DIR = os.path.join(BASE_DIR, "wiki_corpus")
FAILURES_LOG_PATH = os.path.join(BASE_DIR, "fetch_failures.json")

# Wikipedia API Configuration
WIKI_API_URL = "https://en.wikipedia.org/w/api.php"
HEADERS = {
    "User-Agent": "SmartMCQSolverBot/1.0 (https://github.com/example/mcq-solver; contact: student@example.com)"
}
MAX_WORKERS = 4
MAX_RETRIES = 5
DELAY_BETWEEN_REQ = 0.25
TOP_K_ARTICLES = 3



_PUNCT_MAP = {
    "‐": "-", "‑": "-", "‒": "-",   # hyphen variants
    "–": "-", "—": "-", "―": "-",   # en dash, em dash, horizontal bar
    "‘": "", "’": "", "‚": "", "‛": "",   # single quotes
    "“": "", "”": "", "„": "", "‟": "",   # double quotes
    "′": "", "″": "",                    # prime, double prime
    " ": " ",                                 # non-breaking space
    "'": "", '"': "",                              # ASCII quotes
}
_PUNCT_MAP.update({
    "&": " and ", "°": "deg", "±": "pm", "×": "x", "÷": "div",
    "→": "to", "∞": "inf", "≈": "approx", "≠": "ne", "≤": "le", "≥": "ge",
})

_GREEK_MAP = {
    "α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "ε": "epsilon",
    "ζ": "zeta", "η": "eta", "θ": "theta", "ι": "iota", "κ": "kappa",
    "λ": "lambda", "μ": "mu", "ν": "nu", "ξ": "xi", "ο": "omicron",
    "π": "pi", "ρ": "rho", "σ": "sigma", "ς": "sigma", "τ": "tau",
    "υ": "upsilon", "φ": "phi", "χ": "chi", "ψ": "psi", "ω": "omega",
}
_GREEK_MAP.update({g.upper(): n.capitalize() for g, n in list(_GREEK_MAP.items())})
_PUNCT_MAP.update(_GREEK_MAP)

_UNSAFE_FILENAME_CHARS = re.compile(r"[^A-Za-z0-9._-]")
_MAX_STEM_LEN = 120  


def title_to_filename(title: str) -> str:
    text = str(title).strip()
    for src, dst in _PUNCT_MAP.items():
        text = text.replace(src, dst)

    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")

    text = _UNSAFE_FILENAME_CHARS.sub("_", text)
    text = re.sub(r"_{2,}", "_", text).strip("._-")
    return f"{text[:_MAX_STEM_LEN] or 'untitled'}.md"


def normalize_title(title: str) -> str:
    return re.sub(r"\s+", " ", str(title).replace("_", " ")).strip().casefold()


def scan_existing_titles(cache_dir: str) -> dict:
   
    known = {}
    if not os.path.isdir(cache_dir):
        return known

    for name in os.listdir(cache_dir):
        if not name.endswith(".md"):
            continue
        path = os.path.join(cache_dir, name)
        try:
            if os.path.getsize(path) <= 100:
                continue
            with open(path, "r", encoding="utf-8") as f:
                head = f.read(2048)
        except OSError:
            continue

        match = re.match(r"#\s+(.+)", head)
        if not match:
            match = re.search(r"\*\*Wikipedia Page\*\*:\s*\S+/wiki/(\S+)", head)
        if match:
            key = normalize_title(match.group(1))
            if key not in known:
                known[key] = name
                USED_FILENAMES[name] = key

    return known


_titles_lock = threading.Lock()
EXISTING_TITLES = {}   # normalized title -> filename
USED_FILENAMES = {}    # filename -> normalized title


def claim_article(title: str) -> str | None:
    
    key = normalize_title(title)
    with _titles_lock:
        if key in EXISTING_TITLES:
            return None

        filename = title_to_filename(title)
        if USED_FILENAMES.get(filename, key) != key:
            stem, ext = os.path.splitext(filename)
            filename = f"{stem}_{hashlib.md5(key.encode('utf-8')).hexdigest()[:6]}{ext}"

        EXISTING_TITLES[key] = filename
        USED_FILENAMES[filename] = key
        return filename


def release_title(title: str) -> None:
    """Undo a claim when the download turns out to fail, so a retry can pick it up."""
    key = normalize_title(title)
    with _titles_lock:
        filename = EXISTING_TITLES.pop(key, None)
        if filename:
            USED_FILENAMES.pop(filename, None)


def make_wikipedia_api_request(params: dict, session: requests.Session) -> dict | None:
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


# fetch clean markdown, with real formulas

USE_HTML_API = True

REST_HTML_URL = "https://en.wikipedia.org/api/rest_v1/page/html/{}"

# Sections that hold only link lists and citations.
TAIL_SECTIONS = {
    "see also", "references", "further reading", "external links",
    "notes", "bibliography", "sources", "citations", "works cited",
}

DROP_SELECTORS = [
    "style", "script", "table", "figure", "figcaption", "img", "audio", "video",
    "sup.mw-ref", "sup.reference", "span.mw-editsection", "link", "meta",
    "div.hatnote", "div.navbox", "ol.references", "span.mw-cite-backlink",
]


def _tex_of(node) -> str:
    """Pull the original TeX out of a <math> element."""
    annotation = node.find("annotation", attrs={"encoding": "application/x-tex"})
    tex = (annotation.get_text() if annotation else node.get("alttext") or "").strip()
    # Wikipedia wraps display maths as "{\displaystyle ... }"; drop the wrapper.
    match = re.match(r"^\{\\displaystyle\s(.*)\}$", tex, re.S)
    if match:
        tex = match.group(1)
    return re.sub(r"\s+", " ", tex).strip()


def html_to_markdown(html: str) -> str:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "lxml")

    for node in soup.find_all("math"):
        tex = _tex_of(node)
        node.replace_with(f" ${tex}$ " if tex else " ")

    for selector in DROP_SELECTORS:
        for element in soup.select(selector):
            element.decompose()

    blocks = []
    for el in (soup.body or soup).find_all(["h2", "h3", "h4", "p", "li", "dd"]):
        if el.name in ("h2", "h3", "h4"):
            heading = re.sub(r"\s+", " ", el.get_text(" ", strip=True))
            if el.name == "h2" and heading.lower().strip() in TAIL_SECTIONS:
                break
            if heading:
                blocks.append("\n" + "#" * int(el.name[1]) + " " + heading)
            continue
        text = re.sub(r"[ \t]+", " ", el.get_text(" ", strip=True)).strip()
        if len(text) < 2:
            continue
        blocks.append(f"- {text}" if el.name == "li" else text)

    markdown = re.sub(r"\n{3,}", "\n\n", "\n\n".join(blocks))
    return re.sub(r"[ \t]+\$", " $", markdown).strip()


def fetch_wikipedia_html(title: str, session: requests.Session) -> str | None:
    """Fetch a page as Parsoid HTML and convert it to clean markdown."""
    url = REST_HTML_URL.format(quote(title.replace(" ", "_"), safe=""))
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(url, headers=HEADERS, timeout=30)
            if resp.status_code == 429:
                time.sleep(int(resp.headers.get("Retry-After", attempt * 2)))
                continue
            if resp.status_code == 200:
                return html_to_markdown(resp.text)
            if resp.status_code == 404:
                return None
        except (requests.RequestException, ValueError):
            time.sleep(attempt * 1.5)
        time.sleep(DELAY_BETWEEN_REQ)
    return None


def fetch_wikipedia_text(title: str, session: requests.Session) -> str | None:
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
    topic = row["topic"]

    time.sleep(DELAY_BETWEEN_REQ)

    wiki_titles = search_wikipedia_titles(topic, session, top_k=TOP_K_ARTICLES)
    if not wiki_titles:
        return {"topic": topic, "status": "search_failed", "error": "No Wikipedia search match found"}

    example_id = row.get("example_row_id", "N/A")
    source = row.get("source", "N/A")
    freq = row.get("frequency", 1)

    saved_titles = []
    skipped_titles = []

    for rank, wiki_title in enumerate(wiki_titles, start=1):
        filename = claim_article(wiki_title)
        if filename is None:
            skipped_titles.append(wiki_title)
            continue

        target_filepath = os.path.join(CACHE_DIR, filename)
        time.sleep(DELAY_BETWEEN_REQ)

        content = None
        if USE_HTML_API:
            content = fetch_wikipedia_html(wiki_title, session)
        if not content or len(content.strip()) < 100:

            # fall back to the plaintext extract rather than losing the article.
            content = fetch_wikipedia_text(wiki_title, session)
        if not content or len(content.strip()) < 100:
            release_title(wiki_title)  
            continue

        markdown_doc = f"""# {wiki_title}

> **Query Topic**: {topic} (Rank #{rank} Search Result)
> **Source Queue**: {source} (Row ID: {example_id}, Frequency: {freq})
> **Wikipedia Page**: https://en.wikipedia.org/wiki/{wiki_title.replace(' ', '_')}

---

{content.strip()}
"""
        with open(target_filepath, "w", encoding="utf-8") as f:
            f.write(markdown_doc)

        saved_titles.append(wiki_title)

    if not saved_titles and not skipped_titles:
        return {"topic": topic, "status": "fetch_failed", "error": "Empty or short article content for all results"}

    if not saved_titles:
        return {"topic": topic, "status": "already_cached", "skipped_titles": skipped_titles}

    return {
        "topic": topic,
        "status": "success",
        "saved_count": len(saved_titles),
        "saved_titles": saved_titles,
        "skipped_titles": skipped_titles,
    }


def main():
    if not os.path.exists(QUEUE_PATH):
        print(f"Error: Queue CSV file not found at {QUEUE_PATH}")
        return

    print(f"Using manually checked queue: {QUEUE_PATH}")
    queue_df = pd.read_csv(QUEUE_PATH)
    print(f"Loaded {len(queue_df)} topics to process (fetching Top {TOP_K_ARTICLES} Wikipedia articles per topic).")

    os.makedirs(CACHE_DIR, exist_ok=True)

    global EXISTING_TITLES
    EXISTING_TITLES = scan_existing_titles(CACHE_DIR)
    n_files = len([f for f in os.listdir(CACHE_DIR) if f.endswith(".md")])
    print(f"Corpus already holds {len(EXISTING_TITLES)} distinct articles across {n_files} files.")
    if n_files > len(EXISTING_TITLES):
        print(f"  ({n_files - len(EXISTING_TITLES)} of those files are duplicate copies of an "
              f"article stored under another name — legacy topic-based filenames.)")

    topic_records = queue_df.to_dict("records")

    already_cached = 0
    newly_fetched = 0
    articles_saved = 0
    failed = []

    print(f"\nFetching Top {TOP_K_ARTICLES} Wikipedia articles using {MAX_WORKERS} rate-limited threads...")
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        with requests.Session() as session:
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
                    articles_saved += res.get("saved_count", 0)
                else:
                    failed.append(res)

    print("\n" + "=" * 50)
    print(" FETCH SUMMARY REPORT")
    print("=" * 50)
    print(f"Total topics in queue    : {len(topic_records)}")
    print(f"Already fully cached     : {already_cached} (skipped)")
    print(f"Topics with new articles : {newly_fetched}")
    print(f"New articles downloaded  : {articles_saved}")
    print(f"Failed topics            : {len(failed)}")
    print(f"Distinct articles held   : {len(EXISTING_TITLES)}")
    print(f"Wiki Corpus directory    : {CACHE_DIR}")

    if failed:
        with open(FAILURES_LOG_PATH, "w", encoding="utf-8") as f:
            json.dump(failed, f, indent=2)
        print(f"\n⚠️  Saved {len(failed)} failed topic details to: {FAILURES_LOG_PATH}")
        print("First 5 failed topics:")
        for fail in failed[:5]:
            print(f"  - {fail['topic']}: {fail.get('error')}")


if __name__ == "__main__":
    main()
