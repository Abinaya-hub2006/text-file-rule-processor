# 🚀 Task 3 – Performance & Optimization Test

## 📌 Objective

The objective of Task 3 was to:

- Process **1,000,000 records**
- Apply rule-based sentiment scoring
- Insert the scored data into a SQLite database
- Run benchmark queries and measure execution time
- Apply database optimization techniques (indexing)
- Re-run queries and compare performance

---

## ⚙️ Implementation Details

### 1️⃣ Data Processing

- Generated 1,000,000 synthetic review records
- Applied rule-based scoring logic
- Assigned sentiment:
  - Positive
  - Negative
  - Neutral
- Used generator-based record creation for memory efficiency

---

### 2️⃣ Database Operations

- Created table: `performance_test`
- Inserted all records using bulk insertion (`executemany`)
- Measured total insertion time

---

## 📊 Execution Results

| Metric | Time |
|--------|------|
| Insertion Time | **3.49 seconds** |
| Query Time (Before Index) | **0.84 seconds** |
| Query Time (After Index) | **0.69 seconds** |

---

## 🔧 Optimization Applied

Indexes were created on frequently queried columns:

```sql
CREATE INDEX idx_sentiment ON performance_test(sentiment);
CREATE INDEX idx_score ON performance_test(score);