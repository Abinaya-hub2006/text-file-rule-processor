"""
Task 3: Performance & Optimization Test
Process 1 million records using rule-based scoring
Measure query performance before and after indexing
"""

import os
import sqlite3
import time
import random

# -------------------------------
# Simple scoring rules (reuse logic)
# -------------------------------
POSITIVE = ["excellent", "amazing", "great", "fantastic"]
NEGATIVE = ["worst", "terrible", "bad", "awful"]


def calculate_score(text):
    score = 0
    text = text.lower()

    for word in POSITIVE:
        if word in text:
            score += 3

    for word in NEGATIVE:
        if word in text:
            score -= 3

    return score


def assign_sentiment(score):
    if score > 2:
        return "Positive"
    elif score < -2:
        return "Negative"
    else:
        return "Neutral"


# -------------------------------
# DB Setup
# -------------------------------
BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "database", "performance.db")


def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS performance_test")

    cursor.execute("""
        CREATE TABLE performance_test (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            review TEXT,
            score INTEGER,
            sentiment TEXT
        )
    """)

    conn.commit()
    conn.close()


# -------------------------------
# Generate 1M Records
# -------------------------------
def generate_records(n=1_000_000):
    sample_texts = [
        "This movie was amazing and fantastic",
        "Worst film ever terrible experience",
        "It was okay not great not bad",
        "Excellent performance and great acting",
        "Awful waste of time bad movie"
    ]

    for _ in range(n):
        text = random.choice(sample_texts)
        score = calculate_score(text)
        sentiment = assign_sentiment(score)
        yield (text, score, sentiment)


# -------------------------------
# Insert Records
# -------------------------------
def insert_records():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    start = time.time()

    cursor.executemany("""
        INSERT INTO performance_test (review, score, sentiment)
        VALUES (?, ?, ?)
    """, generate_records())

    conn.commit()
    end = time.time()

    conn.close()
    return end - start


# -------------------------------
# Run Query Test
# -------------------------------
def run_queries():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    start = time.time()

    cursor.execute("SELECT COUNT(*) FROM performance_test WHERE sentiment='Positive'")
    cursor.fetchone()

    cursor.execute("SELECT AVG(score) FROM performance_test")
    cursor.fetchone()

    cursor.execute("SELECT * FROM performance_test WHERE score > 2")
    cursor.fetchall()

    end = time.time()
    conn.close()

    return end - start


# -------------------------------
# Add Index Optimization
# -------------------------------
def add_indexes():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("CREATE INDEX idx_sentiment ON performance_test(sentiment)")
    cursor.execute("CREATE INDEX idx_score ON performance_test(score)")

    conn.commit()
    conn.close()


# -------------------------------
# Main Execution
# -------------------------------
def main():
    print("\n--- TASK 3: PERFORMANCE TEST ---\n")

    print("Creating table...")
    create_table()

    print("Inserting 1,000,000 records...")
    insert_time = insert_records()
    print(f"Insertion Time: {insert_time:.2f} seconds")

    print("\nRunning queries WITHOUT index...")
    before_time = run_queries()
    print(f"Query Time Before Index: {before_time:.2f} seconds")

    print("\nApplying Index Optimization...")
    add_indexes()

    print("Running queries WITH index...")
    after_time = run_queries()
    print(f"Query Time After Index: {after_time:.2f} seconds")

    improvement = before_time - after_time
    percentage = (improvement / before_time) * 100 if before_time > 0 else 0

    print("\n--- PERFORMANCE SUMMARY ---")
    print(f"Improvement: {improvement:.2f} seconds faster")
    print(f"Performance Gain: {percentage:.2f}%")


if __name__ == "__main__":
    main()