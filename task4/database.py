import sqlite3
import os
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
DB_DIR = os.path.join(BASE_DIR, "database")
DB_PATH = os.path.join(DB_DIR, "sentiment.db")

if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)


def ensure_db():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS text_analysis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        chunk TEXT,
        score INTEGER,
        sentiment TEXT,
        matched_rules TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_record(filename, chunk, score, sentiment, matched_rules):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO text_analysis
    (filename, chunk, score, sentiment, matched_rules, timestamp)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (filename, chunk, score, sentiment, matched_rules, timestamp))

    conn.commit()
    conn.close()


def fetch_records():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT filename, chunk, score, sentiment, matched_rules, timestamp
    FROM text_analysis
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def fetch_file_records(filename):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT filename, chunk, score, sentiment, matched_rules, timestamp
    FROM text_analysis
    WHERE filename = ?
    ORDER BY id DESC
    """, (filename,))

    rows = cursor.fetchall()

    conn.close()

    return rows

def fetch_file_history():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT DISTINCT filename
    FROM text_analysis
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return [r[0] for r in rows]

ensure_db()