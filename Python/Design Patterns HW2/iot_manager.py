# iot_manager.py

import random
import time

class IoTDevice:
    """
    A base class representing an IoT device in the smart city system.
    """

    def __init__(self, device_id, device_type):
        """
        Initialize an IoT device.

        Args:
            device_id (str): Unique identifier for the device.
            device_type (str): Type of the device (e.g., 'sensor', 'camera').
        """
        self.device_id = device_id
        self.device_type = device_type
        self.status = "Active"

    def get_data(self):
        """
        Simulate data generation from the IoT device.

        Returns:
            dict: Data generated by the device.
        """
        return {"device_id": self.device_id, "status": self.status}


class TrafficSensor(IoTDevice):
    """
    A specialized IoT device class for traffic sensors.
    """

    def get_data(self):
        """
        Simulate traffic sensor data.

        Returns:
            dict: Traffic data.
        """
        data = super().get_data()
        data["traffic_level"] = random.randint(1, 10)  # Simulate traffic level (1-10)
        data["location"] = f"Sector-{random.randint(1, 5)}"
        return data


class IoTManager:
    """
    A class to manage IoT devices in the smart city system.
    """

    def __init__(self):
        self.devices = {}  # Dictionary to store IoT devices by ID

    def register_device(self, device):
        """
        Register an IoT device.

        Args:
            device (IoTDevice): An instance of an IoT device.
        """
        self.devices[device.device_id] = device
        print(f"Device {device.device_id} of type {device.device_type} registered.")

    def collect_data(self):
        """
        Collect data from all registered IoT devices.

        Returns:
            list: A list of data dictionaries from all devices.
        """
        collected_data = []
        for device in self.devices.values():
            collected_data.append(device.get_data())
        return collected_data

# Example usage
if __name__ == "__main__":
    manager = IoTManager()

    # Register devices
    sensor1 = TrafficSensor("sensor1", "TrafficSensor")
    sensor2 = TrafficSensor("sensor2", "TrafficSensor")
    manager.register_device(sensor1)
    manager.register_device(sensor2)

    # Collect data
    while True:
        data = manager.collect_data()
        print("Collected IoT Data:", data)
        time.sleep(5)  # Simulate data collection interval
