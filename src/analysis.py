import pandas as pd

def get_greenest_hours(df: pd.DataFrame, top_n=10) -> pd.DataFrame:
    df = df.sort_values("taux_co2")
    return df.head(top_n)[["date_heure", "taux_co2", "consommation"]]
