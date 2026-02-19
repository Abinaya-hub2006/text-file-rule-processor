"""
SQLite Database Layer
"""

import sqlite3
import os
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "database", "sentiment.db")


def create_table():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS imdb_sentiments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                review TEXT,
                score INTEGER,
                sentiment TEXT,
                timestamp TEXT
            )
        """)

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print("Database error (create table):", e)


def insert_bulk(records):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data = [
            (review, score, sentiment, timestamp)
            for review, score, sentiment in records
        ]

        cursor.executemany("""
            INSERT INTO imdb_sentiments (review, score, sentiment, timestamp)
            VALUES (?, ?, ?, ?)
        """, data)

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print("Database error (insert):", e)

def fetch_and_print(limit=10):
    """
    Fetch and print stored records from database
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT review, score, sentiment, timestamp
            FROM imdb_sentiments
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))

        rows = cursor.fetchall()

        conn.close()

        if not rows:
            print("No records found in database.")
            return

        print("\n--- Showing Stored Records ---\n")

        for i, row in enumerate(rows, 1):
            review, score, sentiment, timestamp = row

            print(f"Record {i}")
            print("Review:", review[:150], "...")  # print first 150 chars only
            print("Score:", score)
            print("Sentiment:", sentiment)
            print("Timestamp:", timestamp)
            print("-" * 60)

    except sqlite3.Error as e:
        print("Database fetch error:", e)

