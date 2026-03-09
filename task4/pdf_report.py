from fpdf import FPDF
from database import fetch_records


def generate_pdf():

    records = fetch_records()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Text Analysis Report", ln=True)

    for r in records[:30]:
        line = f"{r[0]} | Score:{r[2]} | Sentiment:{r[3]}"
        pdf.cell(200, 8, line, ln=True)

    file_name = "report.pdf"
    pdf.output(file_name)

    return file_name