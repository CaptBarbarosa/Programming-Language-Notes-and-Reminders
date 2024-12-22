# resident_portal.py

import tkinter as tk
from tkinter import messagebox


class ResidentPortal:
    """
    A class to create the Resident Portal for the Smart City system.
    """

    def __init__(self, root):
        """
        Initialize the Resident Portal.

        Args:
            root (tk.Tk): Tkinter root window.
        """
        self.root = root
        self.root.title("Resident Portal")
        self.root.geometry("600x400")

        # Title Label
        tk.Label(self.root, text="Resident Portal", font=("Arial", 20)).pack(pady=10)

        # Device Control Button
        tk.Button(self.root, text="Control Home Devices", command=self.control_devices).pack(pady=10)

        # View Utility Bills Button
        tk.Button(self.root, text="View Utility Bills", command=self.view_bills).pack(pady=10)

        # Report Issue Button
        tk.Button(self.root, text="Report an Issue", command=self.report_issue).pack(pady=10)

    def control_devices(self):
        """
        Simulate home device control.
        """
        # Placeholder for device control logic
        messagebox.showinfo("Device Control", "Control lights, appliances, etc.")

    def view_bills(self):
        """
        Simulate viewing utility bills.
        """
        # Placeholder for utility bill logic
        messagebox.showinfo("Utility Bills", "Viewing your utility bills.")

    def report_issue(self):
        """
        Simulate reporting an issue to the administration.
        """
        # Placeholder for issue reporting logic
        issue = "Water leak in Sector 5"
        messagebox.showinfo("Report Issue", f"Issue reported: {issue}")


# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    portal = ResidentPortal(root)
    root.mainloop()
