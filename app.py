# app.py
import streamlit as st
from pages import dashboard
from pages import about
from src.api_client import fetch_eco2mix_data
from src.data_processing import clean_eco2mix_data
from src.analysis import get_greenest_hours

st.set_page_config(page_title="WattsUp ⚡", layout="wide")

st.sidebar.title("WattsUp ⚡")
st.sidebar.subheader("Navigation")
page = st.sidebar.selectbox("Aller à :", ["Dashboard", "À propos"])

rows = st.sidebar.slider("Nombre de points à charger :", 100, 3000, 1000, step=100)

with st.spinner("Chargement des données..."):
    raw_df = fetch_eco2mix_data(rows)
    df = clean_eco2mix_data(raw_df)

if page == "Dashboard":
    dashboard.show(df)

elif page == "À propos":
    about.show()
