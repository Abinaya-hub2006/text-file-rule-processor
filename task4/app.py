# task4/app.py

import streamlit as st
from rules import calculate_score, assign_sentiment
from database import ensure_db, insert_record, fetch_records

st.set_page_config(page_title="Task 4 - Sentiment App", layout="wide")

st.title("📄 Task 4 - Text File Sentiment Analyzer")

ensure_db()

# -----------------------------
# Sidebar Section
# -----------------------------
st.sidebar.header("📂 Uploaded Files")

uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

if uploaded_file is not None:
    st.sidebar.success(f"Uploaded: {uploaded_file.name}")

    content = uploaded_file.read().decode("utf-8")

    st.subheader("📜 File Content")
    st.text_area("Preview", content, height=200)

    score = calculate_score(content)
    sentiment = assign_sentiment(score)

    st.subheader("📊 Analysis Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Score", score)

    with col2:
        if sentiment == "Positive":
            st.success(sentiment)
        elif sentiment == "Negative":
            st.error(sentiment)
        else:
            st.info(sentiment)

    # Save to database
    insert_record(uploaded_file.name, content, score, sentiment)

    st.success("Saved to Database ✅")

# -----------------------------
# Display Database Records
# -----------------------------
st.markdown("---")
st.header("📋 Stored Records")

records = fetch_records()

if records:
    st.dataframe(
        records,
        use_container_width=True
    )
else:
    st.info("No records found in database.")