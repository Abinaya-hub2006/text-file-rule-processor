import streamlit as st
import pandas as pd

from rules import analyze_text
from database import insert_record
from ui import load_css

# Load custom UI style
load_css()

st.title("📂 Upload File for Analysis")

st.write("Upload a **TXT** or **CSV** file to perform rule-based sentiment analysis.")

uploaded_file = st.file_uploader(
    "Upload TXT or CSV file",
    type=["txt", "csv"]
)

if uploaded_file:

    filename = uploaded_file.name
    chunks = []

    # ----------------------------
    # Handle TXT File
    # ----------------------------
    if filename.endswith(".txt"):

        text = uploaded_file.read().decode("utf-8")
        chunks = text.split("\n")

    # ----------------------------
    # Handle CSV File
    # ----------------------------
    elif filename.endswith(".csv"):

        df = pd.read_csv(uploaded_file)

        # Detect possible text column
        possible_cols = ["review", "comment", "text", "sentence"]

        detected_column = None

        for col in df.columns:
            if col.lower() in possible_cols:
                detected_column = col
                break

        if detected_column:
            chunks = df[detected_column].dropna().tolist()
        else:
            # fallback column
            chunks = df.iloc[:, 1].dropna().tolist()

        st.write("Preview of uploaded dataset")
        st.dataframe(df.head())

    # ----------------------------
    # Process Text Chunks
    # ----------------------------
    results = []

    for chunk in chunks:

        chunk = str(chunk).strip()

        if chunk == "":
            continue

        score, sentiment, rules = analyze_text(chunk)

        results.append({
            "Chunk": chunk,
            "Score": score,
            "Sentiment": sentiment,
            "Matched Rules": rules
        })

        insert_record(
            filename,
            chunk,
            score,
            sentiment,
            rules
        )

    # Store results for charts page
    st.session_state["results"] = results

    # ----------------------------
    # Display Results
    # ----------------------------
    st.success(f"Analyzed {len(results)} rows from file.")

    results_df = pd.DataFrame(results)

    st.dataframe(
        results_df,
        use_container_width=True
    )

    # ----------------------------
    # Quick Summary
    # ----------------------------
    st.subheader("📊 Sentiment Summary")

    sentiment_counts = results_df["Sentiment"].value_counts()

    col1, col2, col3 = st.columns(3)

    col1.metric("Positive", sentiment_counts.get("Positive", 0))
    col2.metric("Neutral", sentiment_counts.get("Neutral", 0))
    col3.metric("Negative", sentiment_counts.get("Negative", 0))