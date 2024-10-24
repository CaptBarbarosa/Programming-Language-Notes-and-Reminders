import customtkinter as ctk
from PIL import Image
import os
import sys

# Configure the appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AdminPanel(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Super Admin Panel")
        self.geometry("1100x700")

        # Configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create sidebar frame
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Logo label
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Super Admin Panel",
                                     font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Sidebar buttons
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text="Dashboard",
                                            command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, text="Users",
                                            command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, text="Analytics",
                                            command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        # Appearance mode
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_menu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                    command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=(10, 10))

        # Create main frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Main frame elements
        self.main_label = ctk.CTkLabel(self.main_frame, text="Admin Management",
                                     font=ctk.CTkFont(size=24, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Create tabview
        self.tabview = ctk.CTkTabview(self.main_frame)
        self.tabview.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.tab_1 = self.tabview.add("Admin List")
        self.tab_2 = self.tabview.add("Add Admin")

        # Admin List tab
        self.admin_list_frame = ctk.CTkFrame(self.tab_1)
        self.admin_list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Headers
        headers = ["ID", "Name", "Email", "Actions"]
        for i, header in enumerate(headers):
            label = ctk.CTkLabel(self.admin_list_frame, text=header, font=ctk.CTkFont(weight="bold"))
            label.grid(row=0, column=i, padx=10, pady=5)

        # Sample data
        sample_data = [
            ("1", "Deren", "derentheswimmer@example.com"),
            ("2", "Mete", "aselsanmete@example.com"),
            ("3", "Eray", "gigachaderay@example.com")
        ]

        for i, (id_, name, email) in enumerate(sample_data, start=1):
            ctk.CTkLabel(self.admin_list_frame, text=id_).grid(row=i, column=0, padx=10, pady=5)
            ctk.CTkLabel(self.admin_list_frame, text=name).grid(row=i, column=1, padx=10, pady=5)
            ctk.CTkLabel(self.admin_list_frame, text=email).grid(row=i, column=2, padx=10, pady=5)
            
            delete_btn = ctk.CTkButton(self.admin_list_frame, text="Delete",
                                     command=lambda x=i: self.delete_admin(x),
                                     fg_color="#FF5252", hover_color="#FF1744")
            delete_btn.grid(row=i, column=3, padx=10, pady=5)

        # Add Admin tab
        self.entry_name = ctk.CTkEntry(self.tab_2, placeholder_text="Name")
        self.entry_name.pack(padx=20, pady=10, fill="x")
        
        self.entry_email = ctk.CTkEntry(self.tab_2, placeholder_text="Email")
        self.entry_email.pack(padx=20, pady=10, fill="x")
        
        self.add_button = ctk.CTkButton(self.tab_2, text="Add Admin",
                                      command=self.add_admin)
        self.add_button.pack(padx=20, pady=20)

    def sidebar_button_event(self):
        pass

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def delete_admin(self, row):
        print(f"Deleting admin at row {row}")

    def add_admin(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        print(f"Adding admin: {name} ({email})")

if __name__ == "__main__":
    app = AdminPanel()
    app.mainloop()