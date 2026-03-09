import streamlit as st
from pathlib import Path
from ui import load_css

st.set_page_config(
    page_title=" Text Processing Dashboard",
    layout="wide"
)
load_css()
BASE_DIR = Path(__file__).parent
css_path = BASE_DIR / "assets" / "style.css"

if css_path.exists():
    css = css_path.read_text()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.title("  Text Processing Dashboard")

st.markdown("""
Welcome to the **Rule-Based  Text Analyzer**.

This system allows you to:

 Upload text files  
 Perform rule-based sentiment analysis  
 Visualize results  
 Store analysis in database  
 Generate email reports  

Use the **sidebar navigation** to explore features.
""")
st.markdown(
"""
<style>
@keyframes glow {
0% {text-shadow:0 0 5px red;}
50% {text-shadow:0 0 20px red;}
100% {text-shadow:0 0 5px red;}
}

h1 {
animation: glow 3s infinite;
}
</style>
""",
unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📂 Upload Text Files")

with col2:
    st.success("📊 View Analysis Results")

with col3:
    st.warning("📧 Email Reports")

st.divider()
st.caption("Streamlit Text Processing System")

from database import fetch_file_history

st.sidebar.title("📂 Recent Files")

files = fetch_file_history()

for f in files[:5]:
    st.sidebar.write("📄", f)