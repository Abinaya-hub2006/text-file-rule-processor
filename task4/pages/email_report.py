import smtplib
from email.message import EmailMessage


def send_email(receiver_email, pdf_path):

    sender_email = "abinayak829@gmail.com"

    # Gmail App Password (not your Gmail password)
    app_password = "ckfo ynox gzcp ldde"

    msg = EmailMessage()

    msg["Subject"] = "AI Text Processing Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(
        "Hello,\n\nYour sentiment analysis report is attached.\n\nRegards\nAI Dashboard"
    )

    with open(pdf_path, "rb") as f:
        file_data = f.read()

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename="analysis_report.pdf"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

import streamlit as st
from pdf_report import generate_pdf
from email_service import send_email

st.title("📧 Email PDF Report")

st.write("Enter your email to receive the sentiment analysis report.")

email = st.text_input("Enter Email ID")

if st.button("Send PDF Report"):

    if email == "":
        st.warning("Please enter an email address")

    else:
        try:
            # Generate PDF
            pdf_path = generate_pdf()

            # Send email
            send_email(email, pdf_path)

            st.success("✅ Report sent successfully!")

        except Exception as e:
            st.error(f"❌ Error sending email: {e}")