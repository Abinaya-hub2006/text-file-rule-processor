import pandas as pd
import matplotlib.pyplot as plt

from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

from database import fetch_records


# ------------------------------
# Create Sentiment Chart
# ------------------------------
def generate_chart(df):

    sentiment_counts = df["Sentiment"].value_counts()

    plt.figure(figsize=(5,5))
    sentiment_counts.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Sentiment Distribution")
    plt.ylabel("")

    chart_path = "sentiment_chart.png"

    plt.savefig(chart_path)
    plt.close()

    return chart_path


# ------------------------------
# Generate PDF Report
# ------------------------------
def generate_pdf():

    records = fetch_records()

    file_name = "report.pdf"

    styles = getSampleStyleSheet()

    elements = []

    if not records:
        elements.append(
            Paragraph("No records found in database.", styles["Title"])
        )

        doc = SimpleDocTemplate(file_name, pagesize=letter)
        doc.build(elements)

        return file_name


    # ------------------------------
    # Convert DB records → DataFrame
    # ------------------------------
    df = pd.DataFrame(
        records,
        columns=[
            "Filename",
            "Text",
            "Score",
            "Sentiment",
            "Rules",
            "Timestamp"
        ]
    )

    # ------------------------------
    # PAGE 1 — Summary
    # ------------------------------
    elements.append(
        Paragraph("Sentiment Analysis Report", styles["Title"])
    )

    elements.append(Spacer(1,20))

    total = len(df)
    pos = (df["Sentiment"] == "Positive").sum()
    neu = (df["Sentiment"] == "Neutral").sum()
    neg = (df["Sentiment"] == "Negative").sum()

    summary = f"""
    <b>Total Records:</b> {total}<br/>
    <b>Positive:</b> {pos}<br/>
    <b>Neutral:</b> {neu}<br/>
    <b>Negative:</b> {neg}
    """

    elements.append(Paragraph(summary, styles["Normal"]))

    elements.append(PageBreak())

    # ------------------------------
    # PAGE 2 — Sentiment Chart
    # ------------------------------
    chart_path = generate_chart(df)

    elements.append(
        Paragraph("Sentiment Distribution Chart", styles["Heading2"])
    )

    elements.append(Spacer(1,20))

    elements.append(
        Image(chart_path, width=400, height=400)
    )

    elements.append(PageBreak())

    # ------------------------------
    # PAGE 3 — Sample Records Table
    # ------------------------------
    elements.append(
        Paragraph("Sample Analysis Records", styles["Heading2"])
    )

    elements.append(Spacer(1,20))

    data = [["Text", "Score", "Sentiment"]]

    for r in records[:30]:

        text = str(r[1])[:70]
        score = str(r[2])
        sentiment = str(r[3])

        data.append([text, score, sentiment])

    table = Table(
        data,
        colWidths=[350,60,100]
    )

    table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.lightblue),

        ("GRID",(0,0),(-1,-1),1,colors.grey),

        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

        ("ALIGN",(1,1),(-1,-1),"CENTER")

    ]))

    elements.append(table)

    doc = SimpleDocTemplate(
        file_name,
        pagesize=letter
    )

    doc.build(elements)

    return file_name