# task4/app.py

import streamlit as st
from rules import analyze_text
from database import ensure_db, insert_record, fetch_records

st.set_page_config(page_title="Task 4 - Text Analyzer", layout="wide")

st.title("📄 Task 4 - Rule Based Text Analyzer")

ensure_db()

uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:

    content = uploaded_file.read().decode("utf-8")

    st.subheader("Uploaded Content")
    st.text_area("Preview", content, height=200)

    st.subheader("Processing Results")

    chunks = content.split("\n")

    for chunk in chunks:

        if chunk.strip():

            score, sentiment, rules = analyze_text(chunk)

            insert_record(chunk, score, sentiment, rules)

    st.success("Processing completed and stored in database.")

st.markdown("---")

st.header("📊 Stored Records")

records = fetch_records()

if records:
    st.dataframe(
        records,
        use_container_width=True,
        column_config={
            0: "Chunk",
            1: "Score",
            2: "Sentiment",
            3: "Matched Rules",
            4: "Timestamp"
        }
    )
else:
    st.info("No records found.")