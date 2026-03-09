import streamlit as st
import pandas as pd
import plotly.express as px
from database import fetch_file_history, fetch_file_records
from ui import load_css

load_css()

st.title("🗄 Database Records")

# ----------------------------
# File selector
# ----------------------------

files = fetch_file_history()

if not files:
    st.warning("No records available")
    st.stop()

selected_file = st.selectbox(
    "Select File",
    files
)

records = fetch_file_records(selected_file)

df = pd.DataFrame(
    records,
    columns=[
        "Filename",
        "Chunk",
        "Score",
        "Sentiment",
        "Rules",
        "Timestamp"
    ]
)

st.subheader(f"📄 Analysis for: {selected_file}")

st.dataframe(df, width="stretch")

st.divider()

# ----------------------------
# Summary Metrics
# ----------------------------

pos = (df["Sentiment"] == "Positive").sum()
neg = (df["Sentiment"] == "Negative").sum()
neu = (df["Sentiment"] == "Neutral").sum()

c1, c2, c3 = st.columns(3)

c1.metric("Positive", pos)
c2.metric("Neutral", neu)
c3.metric("Negative", neg)

st.divider()

# ----------------------------
# Sentiment Summary Chart
# ----------------------------

summary = df["Sentiment"].value_counts().reset_index()
summary.columns = ["Sentiment","Count"]

fig1 = px.bar(
    summary,
    x="Sentiment",
    y="Count",
    color="Sentiment",
    title="Sentiment Summary",
    color_discrete_map={
        "Positive":"#00ff9f",
        "Neutral":"#ffd166",
        "Negative":"#ff3b3b"
    }
)

st.plotly_chart(fig1, width="stretch")

st.divider()

# ----------------------------
# Score Distribution
# ----------------------------

fig2 = px.histogram(
    df,
    x="Score",
    color="Sentiment",
    title="Score Distribution",
    color_discrete_map={
        "Positive":"#00ff9f",
        "Neutral":"#ffd166",
        "Negative":"#ff3b3b"
    }
)

st.plotly_chart(fig2, width="stretch")

st.divider()

# ----------------------------
# Timeline Chart
# ----------------------------

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

fig3 = px.line(
    df,
    x="Timestamp",
    y="Score",
    title="Sentiment Score Timeline",
    markers=True
)

st.plotly_chart(fig3, width="stretch")