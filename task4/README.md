# AI Text Processing & Sentiment Analysis Dashboard

This project is a **rule-based sentiment analysis system** built using **Python, Streamlit, and SQLite**.  
It allows users to upload text datasets, analyze sentiment using keyword-based scoring rules, visualize results, and generate downloadable/email reports.

---

## 🚀 Features

- 📂 Upload **TXT or CSV files**
- 🧠 Rule-based sentiment scoring
- 🗄 Store processed results in **SQLite database**
- 📊 Interactive dashboard with **charts**
- 📋 View processed records from database
- 📧 Send analysis results via **email as PDF**
- 📄 Automatically generate **multi-page PDF report**
- 🎨 Clean **professional UI (white + sky blue theme)**

---

## 🧠 Sentiment Analysis Method

The project uses a **keyword-based rule engine**:

- ~100 positive keywords
- ~100 negative keywords

Each keyword contributes to a **sentiment score**.

Example:

| Word | Score |
|-----|------|
| amazing | +2 |
| great | +2 |
| terrible | -2 |
| bad | -2 |

