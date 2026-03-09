import smtplib
import os
from email.message import EmailMessage


def send_email(receiver, pdf_file):

    sender = "abinayak829@gmail.com"
    password = os.getenv("EMAIL_PASSWORD")

    msg = EmailMessage()
    msg["Subject"] = "Text Analysis Report"
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content("Attached is your report.")

    with open(pdf_file, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename="report.pdf"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)