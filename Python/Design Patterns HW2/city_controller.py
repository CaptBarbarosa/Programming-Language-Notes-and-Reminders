class CityController:
    """
    A Singleton class to serve as the central controller of the Smart City System.
    """
    _instance = None  # Class variable to hold the single instance of the class

    def __new__(cls, *args, **kwargs):
        """
        Override the default __new__ method to implement Singleton behavior.
        """
        if not cls._instance:
            cls._instance = super(CityController, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            # Ensure initialization only happens once
            self._initialized = True
            self.iot_devices = {}  # Dictionary to store IoT devices (id -> device instance)
            self.analytics_results = {}  # Store results from predictive analytics
            self.gui_instances = {}  # Track active GUI instances
            self.notifications = []  # List to store notification messages

    # IoT Device Management
    def register_device(self, device_id, device_instance):
        """
        Register a new IoT device with the system.

        Args:
            device_id (str): Unique identifier for the device.
            device_instance (object): The device instance to register.
        """
        self.iot_devices[device_id] = device_instance
        print(f"Device {device_id} registered successfully.")

    def remove_device(self, device_id):
        """
        Remove an IoT device from the system.

        Args:
            device_id (str): Unique identifier for the device to remove.
        """
        if device_id in self.iot_devices:
            del self.iot_devices[device_id]
            print(f"Device {device_id} removed successfully.")
        else:
            print(f"Device {device_id} not found.")

    # Predictive Analytics Management
    def update_analytics(self, analytics_type, result):
        """
        Update analytics results.

        Args:
            analytics_type (str): The type of analytics (e.g., 'traffic', 'energy').
            result (dict): The result of the analytics computation.
        """
        self.analytics_results[analytics_type] = result
        print(f"Analytics updated for {analytics_type}: {result}")

    # GUI Management
    def register_gui_instance(self, user_type, gui_instance):
        """
        Register a GUI instance for a user type.

        Args:
            user_type (str): The type of user (e.g., 'administrator', 'resident').
            gui_instance (object): The GUI instance to register.
        """
        self.gui_instances[user_type] = gui_instance
        print(f"GUI instance for {user_type} registered.")

    # Notifications
    def add_notification(self, message):
        """
        Add a notification to the system.

        Args:
            message (str): The notification message.
        """
        self.notifications.append(message)
        print(f"Notification added: {message}")

    def get_notifications(self):
        """
        Retrieve all notifications.

        Returns:
            list: A list of notification messages.
        """
        return self.notifications

    # Example Action
    def emergency_alert(self, alert_type, location):
        """
        Trigger an emergency alert.

        Args:
            alert_type (str): Type of emergency (e.g., 'fire', 'theft').
            location (str): Location of the emergency.
        """
        alert_message = f"Emergency Alert: {alert_type} at {location}"
        self.add_notification(alert_message)
        print(alert_message)

# Example usage (for testing)
if __name__ == "__main__":
    controller = CityController()

    # Register devices
    controller.register_device("Device1", {"type": "Sensor", "status": "Active"})
    controller.register_device("Device2", {"type": "Camera", "status": "Idle"})

    # Update analytics
    controller.update_analytics("traffic", {"congestion_level": "High", "suggestion": "Use Route B"})

    # Trigger an emergency alert
    controller.emergency_alert("fire", "Sector 7G")
    
    # Fetch notifications
    print(controller.get_notifications())
