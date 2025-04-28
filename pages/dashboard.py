# pages/1_Dashboard.py
import streamlit as st
import pandas as pd
from src.analysis import get_greenest_hours
from src.model import train_and_evaluate_model
from src.data_processing import create_training_dataset
from src.predict import predict_tomorrow_co2

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

    st.markdown("---")
    st.header("🔮 Prédiction du taux de CO₂ pour demain")

    features, target = create_training_dataset(df)

    model, mae = train_and_evaluate_model(features, target)

    st.metric(label="Erreur MAE du modèle", value=f"{mae:.2f} gCO₂/kWh")

    # tomorrow_forecast = st.number_input("Prévision de consommation pour demain (MW)", min_value=30000, max_value=100000, value=60000, step=500)
    tomorrow_forecast = df["prevision_j1"].dropna().iloc[-1]
    
    st.info(f"Prévision de consommation utilisée pour demain : **{tomorrow_forecast:.0f} MW**")

    if st.button("Prédire le taux de CO₂ pour demain"):
        tomorrow_datetime = pd.Timestamp.now() + pd.Timedelta(days=1)
        prediction = predict_tomorrow_co2(model, tomorrow_forecast, tomorrow_datetime)
        st.success(f"Taux de CO₂ prédit pour {tomorrow_datetime.strftime('%A %d %B %Y')} : **{prediction:.2f} gCO₂/kWh**")
        
        if prediction < 30:
            st.balloons()
            st.markdown("✅ C'est une excellente journée pour recharger ton VE !")
        elif prediction < 50:
            st.markdown("🔵 Journée correcte pour la recharge.")
        else:
            st.markdown("🔴 Forte empreinte carbone prévue, à éviter si possible.")
