# traffic_predictor.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class TrafficPredictor:
    """
    A class for predicting traffic congestion using historical and real-time data.
    """

    def __init__(self):
        """
        Initialize the TrafficPredictor with a machine learning model.
        """
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.trained = False

    def train_model(self, data):
        """
        Train the prediction model with historical traffic data.

        Args:
            data (pd.DataFrame): Historical data with features and target variables.

        Returns:
            float: Mean Squared Error of the model on the test data.
        """
        # Features: Time, Day, Weather, Previous Traffic Levels
        X = data[["time_of_day", "day_of_week", "weather_condition", "previous_traffic"]]
        y = data["traffic_level"]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)
        self.trained = True

        # Evaluate the model
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f"Model trained. Mean Squared Error: {mse}")
        return mse

    def predict_traffic(self, input_data):
        """
        Predict traffic levels based on real-time input data.

        Args:
            input_data (dict): A dictionary with features like time_of_day, day_of_week, etc.

        Returns:
            float: Predicted traffic level.
        """
        if not self.trained:
            raise ValueError("Model is not trained yet. Train the model with historical data first.")

        features = np.array([
            input_data["time_of_day"],
            input_data["day_of_week"],
            input_data["weather_condition"],
            input_data["previous_traffic"],
        ]).reshape(1, -1)

        return self.model.predict(features)[0]

# Example usage
if __name__ == "__main__":
    # Sample historical data
    data = pd.DataFrame({
        "time_of_day": [8, 9, 10, 11, 12],
        "day_of_week": [1, 2, 3, 4, 5],
        "weather_condition": [0, 1, 0, 0, 1],
        "previous_traffic": [3, 4, 2, 3, 5],
        "traffic_level": [5, 7, 3, 4, 8],
    })

    predictor = TrafficPredictor()
    mse = predictor.train_model(data)

    # Predict traffic
    input_data = {
        "time_of_day": 9,
        "day_of_week": 3,
        "weather_condition": 0,
        "previous_traffic": 3,
    }
    prediction = predictor.predict_traffic(input_data)
    print(f"Predicted Traffic Level: {prediction}")
