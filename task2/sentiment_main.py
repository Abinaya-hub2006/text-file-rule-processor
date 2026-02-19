import os
from sentiment_processor import load_and_process
from sentiment_database import create_table, insert_bulk, fetch_and_print

BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "dataset", "IMDB Dataset.csv")


def main():
    print("Starting Kaggle Sentiment Rule Engine...\n")

    create_table()

    records = load_and_process(DATA_PATH, limit=5000)

    if not records:
        print("No records processed.")
        return

    insert_bulk(records)

    print(f"\nSuccessfully processed and stored {len(records)} reviews.")

    # 🔥 Print DB content
    fetch_and_print(limit=5)


if __name__ == "__main__":
    main()
