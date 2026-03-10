import smtplib
from email.message import EmailMessage

def send_email(receiver_email, pdf_path):

    sender_email = "abinayak829@gmail.com"
    app_password = "ckfo ynox gzcp ldde"


    msg = EmailMessage()

    msg["Subject"] = "Sentiment Analysis Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content("Your sentiment analysis report is attached.")

    with open(pdf_path, "rb") as f:
        file_data = f.read()

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename="report.pdf"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)