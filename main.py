# main.py

from processor import process_files
from database import create_table, insert_result, fetch_all

DATA_FOLDER = "data"

def main():
    # Step 1: Create DB table
    create_table()

    # Step 2: Process text files
    results = process_files(DATA_FOLDER)

    # Step 3: Insert into SQLite
    for result in results:
        insert_result(result)

    # Step 4: Fetch and print output
    stored_data = fetch_all()

    print("\n--- Processed Results ---")
    for row in stored_data:
        print(f"File: {row[0]}")
        print(f"Score: {row[1]}")
        print(f"Matched Keywords: {row[2]}")
        print("-" * 40)


if __name__ == "__main__":
    main()
