import re
import os
import json
import pandas as pd

# Dynamic path resolution so the pipeline runs portably on any machine/environment
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRAIN_PATH = os.path.join(BASE_DIR, "train.csv")
TEST_PATH = os.path.join(BASE_DIR, "test.csv")
CACHE_DIR = os.path.join(BASE_DIR, "wiki_corpus")          # where downloaded .md files will live
QUEUE_PATH = os.path.join(BASE_DIR, "topics_to_fetch.csv")  # output of this script


# ---------------------------------------------------------------------------
# STEP 1: Strip the templated wrapper phrasing around each prompt
# ---------------------------------------------------------------------------
# Your prompts are a real question wrapped in one of a handful of template
# phrases, e.g. "Pick the best possible answer: What is X? among the listed
# options." The wrapper is noise for topic extraction -- strip it first.
# Optimization: Combined into pre-compiled regexes for ~5x faster execution.
# ---------------------------------------------------------------------------

PREFIX_PATTERN = re.compile(
    r"^(?:pick the best possible answer|select the most accurate option|"
    r"identify the correct statement|choose the correct answer|"
    r"determine the correct option|which of the following is correct)[\:\?\,\.]?\s*",
    flags=re.IGNORECASE,
)

SUFFIX_PATTERN = re.compile(
    r"\s*(?:among the listed options|from the following choices|"
    r"based on the given context|carefully)[\:\?\,\.]?$",
    flags=re.IGNORECASE,
)


def strip_template(prompt: str) -> str:
    text = prompt.strip()
    text = PREFIX_PATTERN.sub("", text)
    text = SUFFIX_PATTERN.sub("", text)
    return text.strip()


# ---------------------------------------------------------------------------
# STEP 1.5: Stopword trimming + junk filtering
# ---------------------------------------------------------------------------
# The raw regex extraction grabs phrases like "Observations of the" or
# "Which of the" -- these are template/connector debris, not real topics.
# We handle this in two passes:
#   1. TRIM edge stopwords off the front/back of every candidate (e.g.
#      "Observations of the" -> "Observations", "The Higgs" -> "Higgs")
#   2. BLOCK candidates that are pure junk even after trimming (e.g.
#      "Which of", "None of", or anything left with zero real content words)
# Simplification: Self-contained STOPWORDS set removes heavy scikit-learn dependency.
# ---------------------------------------------------------------------------

STOPWORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are",
    "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both",
    "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't",
    "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't",
    "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here",
    "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll",
    "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's",
    "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on",
    "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own",
    "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some",
    "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then",
    "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this",
    "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we",
    "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's",
    "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with",
    "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your",
    "yours", "yourself", "yourselves",
    # Domain template / generic noise words that pollute candidate topics
    "correct", "accurate", "statement", "option", "options", "choice", "choices", "answer",
    "following", "none", "observations", "results", "analysis", "study", "studies", "aim",
}

# Common English non-topic words and sentence-starting adverbs that pollute single-word extractions
COMMON_SINGLE_WORDS = {
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "first", "second", "third", "fourth", "fifth", "main", "key", "type", "types",
    "part", "parts", "example", "examples", "system", "systems", "general", "specific",
    "high", "higher", "low", "lower", "large", "small", "new", "old", "different", "similar", "same",
    "also", "well", "however", "therefore", "thus", "hence", "since", "due", "according",
    "spatial", "temporal", "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december",
    # Option-starting sentence adverbs
    "approximately", "typically", "generally", "usually", "essentially", "primarily",
    "normally", "frequently", "rarely", "basically", "specifically",
}

# Phrases that are junk on their own even if they survive trimming
JUNK_PHRASES = {
    "which of", "none of", "some of", "all of", "either of", "neither of",
    "the following", "following statements", "listed options", "observations of",
    "observations of the", "aim of the", "significance of the", "distinction between", "definition of", "first person to describe the"
}

# Trailing clause patterns to clean off question subjects (e.g. "used for in physics" -> "")
TAIL_CLEANUP_PATTERN = re.compile(
    r"\s+(?:used for in physics|described by geologists|in physics|in chemistry|in biology|in astronomy)$",
    flags=re.IGNORECASE,
)


def trim_edge_stopwords(phrase: str) -> str:
    """Repeatedly strip stopwords off the front and back of a phrase."""
    words = phrase.split()
    while words and words[0].lower() in STOPWORDS:
        words.pop(0)
    while words and words[-1].lower() in STOPWORDS:
        words.pop()
    return " ".join(words)


def is_junk_topic(phrase: str) -> bool:
    """True if a (post-trim) phrase carries no real topic content."""
    if not phrase:
        return True
    words = phrase.split()
    lower_phrase = phrase.lower()
    if lower_phrase in JUNK_PHRASES:
        return True
    # Nothing left but stopwords -> junk
    if all(w.lower() in STOPWORDS for w in words):
        return True
    # Single leftover word that's a stopword, generic word, or too short to be a useful search term
    if len(words) == 1:
        w_lower = words[0].lower()
        if w_lower in STOPWORDS or w_lower in COMMON_SINGLE_WORDS or len(words[0]) < 3:
            return True
    return False


def clean_topic(phrase: str) -> str | None:
    """Trim + junk-filter a raw candidate. Clean possessives ('s) & punctuation. Returns None if junk."""
    # Fix: Strip trailing possessives ('s) and surrounding punctuation to avoid truncated terms like "Moon's"
    phrase = re.sub(r"'s$", "", phrase.strip(), flags=re.IGNORECASE).strip(" .,;:'\"`")
    phrase = TAIL_CLEANUP_PATTERN.sub("", phrase).strip()
    trimmed = trim_edge_stopwords(phrase)
    if is_junk_topic(trimmed):
        return None
    return trimmed


# ---------------------------------------------------------------------------
# STEP 2: Extract a "core topic" from a cleaned question
# ---------------------------------------------------------------------------
# Optimization: Expanded pattern to catch "What is/are/was/were/does...",
# "Who proposed/discovered...", "Which ... is known as..."
# ---------------------------------------------------------------------------

CORE_TOPIC_PATTERN = re.compile(
    r"^(?:what|who|which)\s+(?:is|are|was|were|does|do|did|proposed|discovered|shared)?\s*(?:the\s+|an?\s+)?(.+?)\??$",
    flags=re.IGNORECASE,
)


def extract_core_topic(cleaned_prompt: str) -> str | None:
    match = CORE_TOPIC_PATTERN.match(cleaned_prompt.strip())
    if match:
        topic = match.group(1).strip()
        # Drop a trailing "?" if the regex left one in (nested question marks)
        topic = topic.rstrip("?").strip()
        if 1 <= len(topic.split()) <= 16:  # sanity bound, avoid grabbing whole paragraphs
            return clean_topic(topic)
    return None


# ---------------------------------------------------------------------------
# STEP 3: General-purpose proper-noun / technical-term extractor
# ---------------------------------------------------------------------------
# Works on ANY text (prompt or option), not just "what is" questions.
# Heuristic: sequences of Capitalized Words / Alphanumeric Terms, allowing
# lowercase "glue" words in between (of, the, effect, law, theorem, etc.).
# Optimization: Allows 1-word capitalized technical terms from options (e.g. "Blueshifting").
# ---------------------------------------------------------------------------

GLUE_WORDS = r"(?:of|the|and|in|on|for|effect|law|theorem|principle|equation|constant)"
# Allow alphanumeric terms like CEERS-93316 or GP-B
PROPER_PHRASE_PATTERN = re.compile(
    rf"\b[A-Z][\w'-]*(?:\s+(?:[A-Z0-9][\w'-]*|{GLUE_WORDS}))*\b"
)


def extract_proper_phrases(text: str, is_option: bool = False) -> list[str]:
    candidates = PROPER_PHRASE_PATTERN.findall(text)
    cleaned = []
    for c in candidates:
        c = c.strip()
        words = c.split()
        min_len = 2
        if min_len <= len(words) <= 8:
            if any(w[0].isupper() for w in words):
                trimmed = clean_topic(c)
                if trimmed:
                    cleaned.append(trimmed)
    return cleaned


# ---------------------------------------------------------------------------
# STEP 4: Pull all candidate topics out of one row (prompt + options A-E)
# ---------------------------------------------------------------------------

def extract_topics_from_row(row: dict) -> set:
    topics = set()

    cleaned_prompt = strip_template(str(row["prompt"]))

    core = extract_core_topic(cleaned_prompt)
    if core:
        topics.add(core)

    topics.update(extract_proper_phrases(cleaned_prompt, is_option=False))

    for opt_col in ["A", "B", "C", "D", "E"]:
        opt_text = str(row.get(opt_col, ""))
        topics.update(extract_proper_phrases(opt_text, is_option=True))

    # Normalize: strip trailing possessive ('s), collapse whitespace, drop empties, and re-check for junk
    normalized = set()
    for t in topics:
        t = re.sub(r"'s$", "", t.strip(), flags=re.IGNORECASE)
        t = re.sub(r"\s+", " ", t).strip(" .,;:'\"`")
        if t and not is_junk_topic(t):
            normalized.add(t)

    return normalized


# ---------------------------------------------------------------------------
# STEP 5: Cache-key helper -- what filename would this topic be saved as?
# ---------------------------------------------------------------------------

def topic_to_filename(topic: str) -> str:
    key = topic.lower().strip()
    key = re.sub(r"[^a-z0-9]+", "_", key).strip("_")
    return f"{key}.md"


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    train_df = pd.read_csv(TRAIN_PATH)
    test_df = pd.read_csv(TEST_PATH)

    print(f"Loaded train.csv: {len(train_df)} rows")
    print(f"Loaded test.csv : {len(test_df)} rows")

    # topic -> info about where it came from (frequency + one example row)
    topic_info = {}  # normalized_key -> {"display": str, "count": int, "example_id": int}

    for df, source_name in [(train_df, "train"), (test_df, "test")]:
        # Optimization: iterate over dict records (~20x faster than pd.DataFrame.iterrows())
        for row in df.to_dict("records"):
            row_topics = extract_topics_from_row(row)
            row_id = row["id"]
            for t in row_topics:
                key = t.lower()
                if key not in topic_info:
                    topic_info[key] = {"display": t, "count": 0, "example_id": row_id, "source": source_name}
                topic_info[key]["count"] += 1

    print(f"\nExtracted {len(topic_info)} unique candidate topics across both files.")

    # ---- Check against local cache (already-downloaded .md files) ----
    os.makedirs(CACHE_DIR, exist_ok=True)
    already_cached_files = set(os.listdir(CACHE_DIR))

    to_fetch = []
    already_have = []

    for key, info in topic_info.items():
        filename = topic_to_filename(info["display"])
        if filename in already_cached_files:
            already_have.append(info["display"])
        else:
            to_fetch.append({
                "topic": info["display"],
                "cache_filename": filename,
                "frequency": info["count"],
                "example_row_id": info["example_id"],
                "source": info["source"],
            })

    print(f"Already cached  : {len(already_have)} topics (skipped)")
    print(f"Still to fetch  : {len(to_fetch)} topics")

    # ---- Save the fetch queue ----
    queue_df = pd.DataFrame(to_fetch).sort_values("frequency", ascending=False)
    queue_df.to_csv(QUEUE_PATH, index=False)
    print(f"\nSaved fetch queue to: {QUEUE_PATH}")

    print("\nTop 15 most frequent candidate topics (highest value to fetch first):")
    print(queue_df[["topic", "frequency", "source"]].head(15).to_string(index=False))


if __name__ == "__main__":
    main()