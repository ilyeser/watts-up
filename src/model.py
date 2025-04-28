from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd
from src.data_processing import create_training_dataset

def train_and_evaluate_model(features: pd.DataFrame, target: pd.DataFrame):
    """
    Train a Random Forest model to predict CO₂ rates 
    and evaluate its performance on a test set.

    Args:
        features (pd.DataFrame): The input features for training.
        target (pd.Series): The target variable (CO₂ rate).

    Returns:
        model: The trained RandomForest model.
        float: The Mean Absolute Error (MAE) on the test set.
    """

    # Split the data into train (80%) and test (20%) sets
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    # Initialize a simple Random Forest Regressor
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=8,
        random_state=42,
        n_jobs=-1
    )

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model using Mean Absolute Error (MAE)
    mae = mean_absolute_error(y_test, y_pred)

    return model, mae
