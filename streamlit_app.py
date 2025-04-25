import streamlit as st
from src.api_client import fetch_eco2mix_data
from src.data_processing import clean_eco2mix_data
from src.analysis import get_greenest_hours

st.set_page_config(page_title="WattsUp", layout="wide")
st.title("🔋 WattsUp – Quand recharger votre VE ?")
st.markdown("Identifiez les **heures les plus vertes** pour recharger votre véhicule électrique ⚡ grâce aux données eco2mix.")

rows = st.slider("Nombre de points de données à charger :", 100, 1000, 500, step=100)

with st.spinner("Chargement des données..."):
    raw_df = fetch_eco2mix_data(rows)
    df = clean_eco2mix_data(raw_df)

if not df.empty:
    st.subheader("📊 Dernières données disponibles")
    st.dataframe(df[["date_heure", "consommation", "taux_co2"]].head(10))

    st.subheader("🌱 Heures les plus vertes")
    green_df = get_greenest_hours(df)
    st.dataframe(green_df)

    st.line_chart(df.set_index("date_heure")[["taux_co2"]])
else:
    st.error("Aucune donnée disponible.")
