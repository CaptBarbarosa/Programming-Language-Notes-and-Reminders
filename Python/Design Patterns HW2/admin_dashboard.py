# admin_dashboard.py

import tkinter as tk
from tkinter import messagebox
from traffic_predictor import TrafficPredictor
from iot_manager import IoTManager


class AdminDashboard:
    """
    A class to create the Administrator Dashboard for the Smart City system.
    """

    def __init__(self, root, traffic_predictor, iot_manager):
        """
        Initialize the Admin Dashboard.

        Args:
            root (tk.Tk): Tkinter root window.
            traffic_predictor (TrafficPredictor): Instance of the traffic predictor.
            iot_manager (IoTManager): Instance of the IoT manager.
        """
        self.root = root
        self.traffic_predictor = traffic_predictor
        self.iot_manager = iot_manager

        self.root.title("Smart City Admin Dashboard")
        self.root.geometry("800x600")

        # Title Label
        tk.Label(self.root, text="Smart City Admin Dashboard", font=("Arial", 20)).pack(pady=10)

        # Real-time IoT Data Button
        tk.Button(self.root, text="View Real-Time IoT Data", command=self.view_realtime_data).pack(pady=10)

        # Predictive Analytics Button
        tk.Button(self.root, text="Run Predictive Traffic Analytics", command=self.run_traffic_prediction).pack(pady=10)

        # Emergency Alerts Button
        tk.Button(self.root, text="View Emergency Alerts", command=self.view_emergency_alerts).pack(pady=10)

    def view_realtime_data(self):
        """
        Display real-time data collected from IoT devices.
        """
        data = self.iot_manager.collect_data()
        data_str = "\n".join([str(device_data) for device_data in data])
        messagebox.showinfo("Real-Time IoT Data", data_str)

    def run_traffic_prediction(self):
        """
        Run predictive traffic analytics and display results.
        """
        # Simulate prediction input
        input_data = {
            "time_of_day": 9,
            "day_of_week": 3,
            "weather_condition": 0,
            "previous_traffic": 3,
        }
        try:
            prediction = self.traffic_predictor.predict_traffic(input_data)
            messagebox.showinfo("Traffic Prediction", f"Predicted Traffic Level: {prediction}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def view_emergency_alerts(self):
        """
        Display emergency alerts stored in the system.
        """
        # Placeholder for emergency alert logic
        messagebox.showinfo("Emergency Alerts", "No active alerts at the moment.")


# Example usage
if __name__ == "__main__":
    from traffic_predictor import TrafficPredictor
    from iot_manager import IoTManager, TrafficSensor

    # Initialize components
    predictor = TrafficPredictor()
    manager = IoTManager()

    # Register IoT devices
    sensor1 = TrafficSensor("sensor1", "TrafficSensor")
    sensor2 = TrafficSensor("sensor2", "TrafficSensor")
    manager.register_device(sensor1)
    manager.register_device(sensor2)

    # Create GUI
    root = tk.Tk()
    dashboard = AdminDashboard(root, predictor, manager)
    root.mainloop()
