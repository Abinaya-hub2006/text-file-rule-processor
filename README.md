# 📚 Text File Rule Processor with SQLite

## 📌 Project Overview

This project reads multiple text files, applies keyword-based scoring rules, stores the processed results in an SQLite database, and prints the stored results in the terminal.

It demonstrates:
- File handling in Python
- Rule-based text processing
- SQLite database integration
- Modular project structure

---

## 📁 Project Structure

text_processor_project/
│
├── data/                # Input text files
│   ├── file1.txt
│   ├── file2.txt
│   └── file3.txt
│
├── database/            # SQLite database (auto-created)
│   └── results.db
│
├── rules.py             # Keyword scoring rules
├── processor.py         # File reading & processing logic
├── database.py          # SQLite database functions
├── main.py              # Entry point
└── README.md

---

## ⚙️ Keyword Scoring Rules

Example rules:

| Keyword           | Score |
|------------------|-------|
| python           | +5    |
| ai               | +10   |
| machine learning | +15   |
| data             | +3    |
| error            | -5    |
| warning          | -2    |

The system calculates total score based on keyword presence in each file.

---

## ▶️ How to Run

1. Open the project folder in VS Code
2. Open terminal
3. Run:

```bash
python main.py
