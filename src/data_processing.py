import pandas as pd

def clean_eco2mix_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["date_heure", "taux_co2", "consommation"])
    df["date_heure"] = pd.to_datetime(df["date_heure"])
    df = df.sort_values("date_heure")
    return df
