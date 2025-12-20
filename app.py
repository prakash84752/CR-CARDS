import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Clash Royale Cards", layout="wide")

# Get directory of app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Excel file path
DATA_PATH = os.path.join(BASE_DIR, "clash_royale_cards.xlsx")

# Load Excel file safely
try:
    data = pd.read_excel(DATA_PATH)
except FileNotFoundError:
    st.error("❌ File 'clash_royale_cards.xlsx' not found.")
    st.write("📂 Files available in app directory:")
    st.write(os.listdir(BASE_DIR))
    st.stop()

# App UI
st.title("🏰 Clash Royale Cards Dataset")

st.subheader("Dataset Preview")
st.dataframe(data)

st.subheader("Dataset Info")
st.write(f"Rows: {data.shape[0]}")
st.write(f"Columns: {data.shape[1]}")
