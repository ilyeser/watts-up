# pages/1_Dashboard.py
import streamlit as st
from src.analysis import get_greenest_hours

def show(df):
    st.title("🔋 Dashboard – Heures vertes pour recharger votre VE")

    if df.empty:
        st.error("Aucune donnée disponible.")
        return

    st.subheader("📊 Dernières données")
    st.dataframe(df.tail(10)[["date_heure", "consommation", "taux_co2"]].tail(10))

    st.subheader("🌱 Heures les plus vertes")
    green_df = get_greenest_hours(df)
    st.dataframe(green_df)

    st.subheader("📈 Taux de CO2")
    st.line_chart(df.set_index("date_heure")[["taux_co2"]])
