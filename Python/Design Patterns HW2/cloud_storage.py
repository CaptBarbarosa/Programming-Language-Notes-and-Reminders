# cloud_storage.py

import os
from cryptography.fernet import Fernet

class CloudStorage:
    """
    A class to handle interactions with hybrid-cloud services for data storage and retrieval.
    """

    def __init__(self, encryption_key=None):
        """
        Initialize the CloudStorage instance.

        Args:
            encryption_key (str): Encryption key for securing data. If None, a new key will be generated.
        """
        if encryption_key is None:
            self.encryption_key = Fernet.generate_key()
            print("New encryption key generated.")
        else:
            self.encryption_key = encryption_key.encode()

        self.cipher = Fernet(self.encryption_key)
        self.storage = {}  # Simulating cloud storage with a dictionary for demo purposes

    def upload_data(self, file_name, data):
        """
        Upload data to the cloud storage.

        Args:
            file_name (str): Name of the file to be stored.
            data (str): The data to be stored.

        Returns:
            str: Confirmation message.
        """
        encrypted_data = self.cipher.encrypt(data.encode())
        self.storage[file_name] = encrypted_data
        return f"Data uploaded and encrypted under file name: {file_name}"

    def retrieve_data(self, file_name):
        """
        Retrieve data from cloud storage.

        Args:
            file_name (str): Name of the file to retrieve.

        Returns:
            str: Decrypted data or error message.
        """
        if file_name not in self.storage:
            return f"File {file_name} not found in cloud storage."

        encrypted_data = self.storage[file_name]
        decrypted_data = self.cipher.decrypt(encrypted_data).decode()
        return decrypted_data

    def delete_data(self, file_name):
        """
        Delete data from cloud storage.

        Args:
            file_name (str): Name of the file to delete.

        Returns:
            str: Confirmation message.
        """
        if file_name in self.storage:
            del self.storage[file_name]
            return f"File {file_name} successfully deleted from cloud storage."
        else:
            return f"File {file_name} not found in cloud storage."

    def list_files(self):
        """
        List all files in the cloud storage.

        Returns:
            list: List of file names stored in the cloud.
        """
        return list(self.storage.keys())

    def export_encryption_key(self, file_path):
        """
        Export the encryption key to a file for safekeeping.

        Args:
            file_path (str): Path to the file where the encryption key will be stored.
        """
        with open(file_path, "wb") as key_file:
            key_file.write(self.encryption_key)
        print(f"Encryption key exported to {file_path}.")

    @staticmethod
    def import_encryption_key(file_path):
        """
        Import an encryption key from a file.

        Args:
            file_path (str): Path to the file containing the encryption key.

        Returns:
            str: Imported encryption key as a string.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Key file {file_path} not found.")

        with open(file_path, "rb") as key_file:
            return key_file.read().decode()

# Example usage (for testing)
if __name__ == "__main__":
    # Initialize cloud storage
    cloud = CloudStorage()

    # Upload some data
    print(cloud.upload_data("traffic_data.json", '{"traffic": "high", "routes": ["A", "B"]}'))
    print(cloud.upload_data("energy_data.json", '{"usage": "low", "capacity": 80}'))

    # Retrieve data
    print(cloud.retrieve_data("traffic_data.json"))
    print(cloud.retrieve_data("energy_data.json"))

    # List files
    print("Files in storage:", cloud.list_files())

    # Delete a file
    print(cloud.delete_data("energy_data.json"))
    print("Files in storage after deletion:", cloud.list_files())

    # Export encryption key
    cloud.export_encryption_key("encryption_key.key")

    # Import encryption key
    imported_key = CloudStorage.import_encryption_key("encryption_key.key")
    print("Imported encryption key:", imported_key)
