# notification_service.py

import smtplib
from email.mime.text import MIMEText


class Observer:
    """
    Base class for observers who wish to receive notifications.
    """

    def update(self, message):
        """
        Receive an update notification.
        Args:
            message (str): The notification message.
        """
        raise NotImplementedError("Subclasses must implement this method.")


class NotificationService:
    """
    A class to manage event-driven notifications using the Observer Pattern.
    """

    def __init__(self):
        """
        Initialize the NotificationService with an empty list of observers.
        """
        self.observers = []

    def subscribe(self, observer):
        """
        Subscribe an observer to the notification service.

        Args:
            observer (Observer): The observer to subscribe.
        """
        self.observers.append(observer)

    def unsubscribe(self, observer):
        """
        Unsubscribe an observer from the notification service.

        Args:
            observer (Observer): The observer to unsubscribe.
        """
        self.observers.remove(observer)

    def notify(self, message):
        """
        Notify all subscribed observers with a message.

        Args:
            message (str): The notification message.
        """
        for observer in self.observers:
            observer.update(message)


class EmailObserver(Observer):
    """
    An observer class to send notifications via email.
    """

    def __init__(self, email_address, smtp_server, smtp_port, smtp_username, smtp_password):
        """
        Initialize the EmailObserver with email server credentials.

        Args:
            email_address (str): The recipient's email address.
            smtp_server (str): SMTP server address.
            smtp_port (int): SMTP server port.
            smtp_username (str): SMTP username.
            smtp_password (str): SMTP password.
        """
        self.email_address = email_address
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password

    def update(self, message):
        """
        Send an email with the given message.

        Args:
            message (str): The notification message.
        """
        try:
            # Create the email
            msg = MIMEText(message)
            msg["Subject"] = "Smart City Notification"
            msg["From"] = self.smtp_username
            msg["To"] = self.email_address

            # Send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.sendmail(self.smtp_username, self.email_address, msg.as_string())

            print(f"Notification sent to {self.email_address}: {message}")
        except Exception as e:
            print(f"Failed to send email to {self.email_address}: {e}")


# Example usage
if __name__ == "__main__":
    # Create the NotificationService
    service = NotificationService()

    # Create an EmailObserver (replace with real credentials for actual use)
    email_observer = EmailObserver(
        email_address="recipient@example.com",
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        smtp_username="your_email@gmail.com",
        smtp_password="your_password",
    )

    # Subscribe the observer to the service
    service.subscribe(email_observer)

    # Notify observers
    service.notify("This is a test notification for the Smart City system.")
