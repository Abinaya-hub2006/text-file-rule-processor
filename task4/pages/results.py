import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from ui import load_css

load_css()

st.title("📊 Sentiment Analysis Results")

# If no file uploaded
if "results" not in st.session_state:

    st.warning("Upload a file first")

else:

    df = pd.DataFrame(st.session_state["results"])

    st.subheader("📄 Chunk Analysis Table")

    st.dataframe(df, width="stretch")

    st.divider()

    # -------------------------
    # Summary Metrics
    # -------------------------

    pos = (df["Sentiment"] == "Positive").sum()
    neg = (df["Sentiment"] == "Negative").sum()
    neu = (df["Sentiment"] == "Neutral").sum()

    c1, c2, c3 = st.columns(3)

    c1.metric("😊 Positive Reviews", pos)
    c2.metric("😐 Neutral Reviews", neu)
    c3.metric("😡 Negative Reviews", neg)

    st.divider()

    # -------------------------
    # Sentiment Distribution
    # -------------------------

    sentiment_counts = df["Sentiment"].value_counts().reset_index()
    sentiment_counts.columns = ["Sentiment","Count"]

    col1, col2 = st.columns(2)

    with col1:

        fig = px.pie(
            sentiment_counts,
            names="Sentiment",
            values="Count",
            title="Sentiment Distribution",
            color="Sentiment",
            color_discrete_map={
                "Positive":"#00ff9f",
                "Neutral":"#ffd166",
                "Negative":"#ff3b3b"
            }
        )

        st.plotly_chart(fig, width="stretch")

    # -------------------------
    # Sentiment Bar Chart
    # -------------------------

    with col2:

        fig2 = px.bar(
            sentiment_counts,
            x="Sentiment",
            y="Count",
            color="Sentiment",
            title="Sentiment Count",
            color_discrete_map={
                "Positive":"#00ff9f",
                "Neutral":"#ffd166",
                "Negative":"#ff3b3b"
            }
        )

        st.plotly_chart(fig2, width="stretch")

    st.divider()

    # -------------------------
    # Sentiment Gauge
    # -------------------------

    st.subheader("📈 Overall Sentiment Score")

    avg_score = df["Score"].mean()

    fig3 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=avg_score,
        title={"text":"Average Sentiment Score"},
        gauge={
            "axis":{"range":[-5,5]},
            "bar":{"color":"red"},
            "steps":[
                {"range":[-5,-1],"color":"#ff4d4d"},
                {"range":[-1,1],"color":"#ffd166"},
                {"range":[1,5],"color":"#00ff9f"}
            ]
        }
    ))

    st.plotly_chart(fig3, width="stretch")

    st.divider()

    # -------------------------
    # Word Cloud
    # -------------------------

    st.subheader("☁ Review Word Cloud")

    text = " ".join(df["Chunk"].astype(str))

    wc = WordCloud(
        width=800,
        height=400,
        background_color="black",
        colormap="Reds"
    ).generate(text)

    fig4, ax = plt.subplots()

    ax.imshow(wc)
    ax.axis("off")

    st.pyplot(fig4)

    st.divider()

    # -------------------------
    # Download Results
    # -------------------------

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Analysis Results",
        csv,
        "sentiment_analysis.csv",
        "text/csv"
    )