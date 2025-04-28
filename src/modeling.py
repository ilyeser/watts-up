from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

def train_co2_model(df: pd.DataFrame):
    features = ["prevision_j1", "solaire", "eolien", "gaz", "fioul", "nucleaire", "hydraulique", "bioenergies"]
    time_features = ["heure", "mois", "jour_semaine"]
    X = df[features + time_features]
    y = df["taux_co2"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"R2 score : {score:.2f}")

    return model