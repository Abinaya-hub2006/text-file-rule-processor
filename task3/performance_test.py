"""
Task 3: Performance & Optimization Test

Process 1 million records using rule-based scoring.
Measure query performance before and after indexing.
Provide detailed comparison for each query.
"""

import os
import sqlite3
import time
import random

# ==========================================================
# 1️⃣ Scoring Rules
# ==========================================================
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


# ==========================================================
# 2️⃣ Database Setup
# ==========================================================
BASE_DIR = os.path.dirname(__file__)
DB_DIR = os.path.join(BASE_DIR, "database")
DB_PATH = os.path.join(DB_DIR, "performance.db")


def ensure_database_directory():
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)


def create_table():
    try:
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

    except sqlite3.Error as e:
        print("Database error (create_table):", e)


# ==========================================================
# 3️⃣ Generate 1 Million Records (Memory Efficient Generator)
# ==========================================================
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


# ==========================================================
# 4️⃣ Insert Records
# ==========================================================
def insert_records():
    try:
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

    except sqlite3.Error as e:
        print("Database error (insert):", e)
        return 0


# ==========================================================
# 5️⃣ Query Benchmark (Each Query Measured Separately)
# ==========================================================
def run_queries():
    results = {}

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Query 1: Count Positive
        start = time.time()
        cursor.execute("SELECT COUNT(*) FROM performance_test WHERE sentiment='Positive'")
        cursor.fetchone()
        results["Count Positive"] = time.time() - start

        # Query 2: Average Score
        start = time.time()
        cursor.execute("SELECT AVG(score) FROM performance_test")
        cursor.fetchone()
        results["Average Score"] = time.time() - start

        # Query 3: Filter High Score
        start = time.time()
        cursor.execute("SELECT * FROM performance_test WHERE score > 2")
        cursor.fetchall()
        results["Filter score > 2"] = time.time() - start

        conn.close()

    except sqlite3.Error as e:
        print("Database error (query):", e)

    return results


# ==========================================================
# 6️⃣ Index Optimization
# ==========================================================
def add_indexes():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sentiment ON performance_test(sentiment)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_score ON performance_test(score)")

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print("Database error (index):", e)


# ==========================================================
# 7️⃣ Main Execution
# ==========================================================
def main():
    print("\n==============================")
    print(" TASK 3: PERFORMANCE TEST")
    print("==============================\n")

    ensure_database_directory()

    print("Creating table...")
    create_table()

    print("Inserting 1,000,000 records...")
    insert_time = insert_records()
    print(f"Insertion Time: {insert_time:.4f} seconds")

    # -------------------------
    # Before Index
    # -------------------------
    print("\nRunning queries WITHOUT index...")
    before_results = run_queries()

    # -------------------------
    # Apply Index
    # -------------------------
    print("\nApplying Index Optimization...")
    add_indexes()

    # -------------------------
    # After Index
    # -------------------------
    print("Running queries WITH index...")
    after_results = run_queries()

    # -------------------------
    # Comparison
    # -------------------------
    print("\n==============================")
    print(" PERFORMANCE COMPARISON")
    print("==============================\n")

    for query in before_results:
        before = before_results[query]
        after = after_results[query]

        improvement = before - after
        percentage = (improvement / before) * 100 if before > 0 else 0

        print(f"Query: {query}")
        print(f"  Before Index : {before:.6f} sec")
        print(f"  After Index  : {after:.6f} sec")
        print(f"  Improvement  : {improvement:.6f} sec")
        print(f"  Gain         : {percentage:.2f}%")
        print("-" * 50)

    print("\nTask 3 Completed Successfully.\n")


if __name__ == "__main__":
    main()