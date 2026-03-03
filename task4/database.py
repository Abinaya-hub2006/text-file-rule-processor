# task4/database.py

import sqlite3
import os
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
DB_DIR = os.path.join(BASE_DIR, "database")
DB_PATH = os.path.join(DB_DIR, "sentiment.db")


def ensure_db():
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS uploaded_texts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            content TEXT,
            score INTEGER,
            sentiment TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_record(filename, content, score, sentiment):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO uploaded_texts (filename, content, score, sentiment, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (filename, content, score, sentiment, timestamp))

    conn.commit()
    conn.close()


def fetch_records():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, filename, score, sentiment, timestamp
        FROM uploaded_texts
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows