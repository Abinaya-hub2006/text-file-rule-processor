from pathlib import Path
import streamlit as st

def load_css():

    BASE_DIR = Path(__file__).parent
    css_path = BASE_DIR / "assets" / "style.css"

    if css_path.exists():
        css = css_path.read_text()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)