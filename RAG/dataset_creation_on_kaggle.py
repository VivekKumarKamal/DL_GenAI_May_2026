import os
import json
from kaggle.api.kaggle_api_extended import KaggleApi

DATASET_DIR = "/Users/vivekkumarkamal/Projects/Coding/DL_GenAI_May_2026/RAG/wiki_corpus"   
DATASET_TITLE = "wiki_corpus_new_top3"
DATASET_SLUG = "wiki_corpus_new_top3"          
KAGGLE_USERNAME = "vivekkumarkamal"
CREATE_NEW = True                          # True = first upload, False = new version of existing dataset
VERSION_NOTES = "Initial upload"  # only used when updatig a existing dataset

def ensure_metadata_file(folder, title, slug, username):
    metadata_path = os.path.join(folder, "dataset-metadata.json")
    if not os.path.exists(metadata_path):
        metadata = {
            "title": title,
            "id": f"{username}/{slug}",
            "licenses": [{"name": "CC0-1.0"}]
        }
        with open(metadata_path, "w") as f:
            json.dump(metadata, f, indent=2)
        print(f"Created {metadata_path}")
    return metadata_path


def main():
    if not os.path.isdir(DATASET_DIR):
        raise FileNotFoundError(f"Folder not found: {DATASET_DIR}")

    ensure_metadata_file(DATASET_DIR, DATASET_TITLE, DATASET_SLUG, KAGGLE_USERNAME)

    api = KaggleApi()
    api.authenticate()  # reads ~/.kaggle/kaggle.json

    if CREATE_NEW:
        print("Creating new dataset on Kaggle...")
        api.dataset_create_new(
            folder=DATASET_DIR,
            public=False,
            quiet=False
        )
    else:
        print("Uploading new version of existing dataset...")
        api.dataset_create_version(
            folder=DATASET_DIR,
            version_notes=VERSION_NOTES,
            quiet=False
        )

    print("Done. Check https://www.kaggle.com/datasets for status.")

if __name__ == "__main__":
    main()