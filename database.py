# database.py

import sqlite3
import os

DB_PATH = os.path.join("database", "results.db")

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            content TEXT,
            score INTEGER,
            keywords TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_result(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO results (filename, content, score, keywords)
        VALUES (?, ?, ?, ?)
    """, (data["filename"], data["content"], data["score"], data["keywords"]))

    conn.commit()
    conn.close()


def fetch_all():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT filename, score, keywords FROM results")
    rows = cursor.fetchall()

    conn.close()
    return rows
