import streamlit as st
import streamlit.components.v1 as components

# Set full-width layout
st.set_page_config(page_title="GBHS MEHRAND", layout="wide")

# Read and render index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=1000, scrolling=True)
