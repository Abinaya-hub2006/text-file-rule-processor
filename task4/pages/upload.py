import streamlit as st
import pandas as pd
from rules import analyze_chunk
from database import insert_record
import streamlit as st
from ui import load_css

load_css()


st.title("📂 Upload File for Analysis")

uploaded_file = st.file_uploader(
    "Upload TXT or CSV file",
    type=["txt","csv"]
)

if uploaded_file:

    filename = uploaded_file.name

    chunks = []

    # TXT FILE
    if filename.endswith(".txt"):

        text = uploaded_file.read().decode()

        chunks = text.split("\n")

    # CSV FILE
    elif filename.endswith(".csv"):

        df = pd.read_csv(uploaded_file)

        # assume reviews column
        if "review" in df.columns:
            chunks = df["review"].dropna().tolist()
        else:
            chunks = df.iloc[:,0].dropna().tolist()

    results = []

    for chunk in chunks:

        chunk = str(chunk).strip()

        if chunk == "":
            continue

        score, sentiment, rules = analyze_chunk(chunk)

        results.append({
            "Chunk": chunk,
            "Score": score,
            "Sentiment": sentiment,
            "Rules": rules
        })

        insert_record(
            filename,
            chunk,
            score,
            sentiment,
            rules
        )

    st.session_state["results"] = results

    st.success(f"Analyzed {len(results)} reviews from file")

    st.dataframe(results, width="stretch")