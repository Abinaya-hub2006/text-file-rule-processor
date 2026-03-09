import streamlit as st
from pdf_report import generate_pdf
from email_service import send_email
import streamlit as st
from ui import load_css

load_css()


st.title("📧 Email PDF Report")

email = st.text_input("Enter Email ID")

if st.button("Send PDF Report"):

    if email == "":
        st.warning("Enter email")

    else:
        try:
            pdf = generate_pdf()
            send_email(email, pdf)
            st.success("Report sent successfully")

        except Exception as e:
            st.error(str(e))