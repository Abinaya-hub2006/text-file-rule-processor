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
        CREATE TABLE IF NOT EXISTS text_analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chunk TEXT,
            score INTEGER,
            sentiment TEXT,
            matched_rules TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_record(chunk, score, sentiment, matched_rules):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO text_analysis (chunk, score, sentiment, matched_rules, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (chunk, score, sentiment, matched_rules, timestamp))

    conn.commit()
    conn.close()


def fetch_records():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT chunk, score, sentiment, matched_rules, timestamp
        FROM text_analysis
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows