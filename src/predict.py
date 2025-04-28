import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def predict_tomorrow_co2(model: RandomForestRegressor, tomorrow_forecast: float, datetime: pd.Timestamp) -> float:
    """
    Predict the CO₂ rate for tomorrow given the consumption forecast 
    and temporal information.

    Args:
        model (RandomForestRegressor): The trained model.
        tomorrow_forecast (float): The consumption forecast for tomorrow (MW).
        datetime (pd.Timestamp): The datetime corresponding to tomorrow's date.

    Returns:
        float: Predicted CO₂ rate (gCO₂/kWh).
    """

    # Create input features (must match training format)
    features = pd.DataFrame({
        "prevision_j1_lag": [tomorrow_forecast],
        "day_of_week": [datetime.dayofweek],  # Monday = 0
        "month": [datetime.month],
        "hour": [datetime.hour]
    })

    # Predict and return
    prediction = model.predict(features)[0]
    print("Prediction done.")
    return prediction
