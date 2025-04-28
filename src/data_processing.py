# src/data_processing.py
import pandas as pd

def clean_eco2mix_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["date_heure", "taux_co2", "consommation"])
    df["date_heure"] = pd.to_datetime(df["date_heure"])
    df = df.sort_values("date_heure")
    return df


def create_training_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a dataset to predict CO₂ rate based on the previous day's consumption forecast 
    and temporal features.
    
    Args:
        df (pd.DataFrame): eco2mix data containing at least ['date_heure', 'prevision_j1', 'taux_co2'] columns.
        
    Returns:
        pd.DataFrame, pd.Series: Features and target ready for training.
    """

    # Ensure datetime format
    df["date_heure"] = pd.to_datetime(df["date_heure"], utc=True)
    
    # Create time-based features
    df["day_of_week"] = df["date_heure"].dt.dayofweek  # 0 = Monday
    df["month"] = df["date_heure"].dt.month
    df["hour"] = df["date_heure"].dt.hour

    # Important: Sort the data by datetime
    df = df.sort_values("date_heure")

    # Shift the consumption forecast to match it with the actual CO₂ rate observed the next day
    df["prevision_j1_lag"] = df["prevision_j1"].shift(1)

    # Drop rows with NaN values created by the shift
    df = df.dropna(subset=["prevision_j1_lag", "taux_co2"])

    # Select only relevant columns
    features = df[[
        "prevision_j1_lag",  # Previous day's consumption forecast
        "day_of_week",
        "month",
        "hour"
    ]]

    target = df["taux_co2"]

    return features, target
