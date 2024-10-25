import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

# Set appearance mode and default color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AdminPanel(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Admin Panel")
        self.geometry("1100x700")
        self.resizable(True, True)

        # Colors (if needed for further customization)
        self.primary_color = "#1f538d"
        self.accent_color = "#ff4757"
        self.bg_color = "#2c3e50"
        self.text_color = "#ffffff"
        self.button_bg_color = "#344b5e"  # Slightly lighter color for buttons

        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create Navigation Frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(10, weight=1)  # Increased to accommodate new button

        # App Title
        self.app_title = ctk.CTkLabel(
            self.navigation_frame,
            text="Admin Panel",
            font=ctk.CTkFont(size=20, weight="bold"),
            pady=20,
            fg_color="transparent"
        )
        self.app_title.grid(row=0, column=0, padx=20)

        # Navigation Buttons
        self.nav_buttons = []
        nav_items = ["Dashboard", "Companies", "Users", "Issues"]  # Added Users

        for i, item in enumerate(nav_items, start=1):
            button = ctk.CTkButton(
                self.navigation_frame,
                corner_radius=0,
                height=40,
                border_spacing=10,
                text=item,
                fg_color=self.button_bg_color,  # Added background color
                text_color=self.text_color,
                hover_color=self.primary_color,
                anchor="w",
                command=lambda x=item: self.nav_button_click(x)
            )
            button.grid(row=i, column=0, sticky="ew", padx=20)
            self.nav_buttons.append(button)

        # Settings Button (Moved to bottom)
        settings_button = ctk.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Settings",
            fg_color=self.button_bg_color,  # Added background color
            text_color=self.text_color,
            hover_color=self.primary_color,
            anchor="w",
            command=lambda: self.nav_button_click("Settings")
        )
        settings_button.grid(row=9, column=0, sticky="ew", padx=20, pady=(0, 10))  # Positioned at bottom
        self.nav_buttons.append(settings_button)

        # Appearance Mode Frame
        self.appearance_mode_frame = ctk.CTkFrame(self.navigation_frame, fg_color="transparent")
        self.appearance_mode_frame.grid(row=10, column=0, padx=20, pady=20, sticky="s")

        self.appearance_mode_label = ctk.CTkLabel(
            self.appearance_mode_frame,
            text="Appearance Mode:",
            anchor="w",
            fg_color="transparent",
            text_color=self.text_color
        )
        self.appearance_mode_label.grid(row=0, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_menu = ctk.CTkOptionMenu(
            self.appearance_mode_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode
        )
        self.appearance_mode_menu.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.appearance_mode_menu.set(ctk.get_appearance_mode())

        # Main Content Frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#2b2b2b")
        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Initialize Data
        self.companies = [
            {"name": "Company A", "location": "Location A"},
            {"name": "Company B", "location": "Location B"}
        ]

        self.users = [
            {"username": "john_doe", "role": "Admin", "status": "Active"},
            {"username": "jane_smith", "role": "User", "status": "Active"}
        ]

        self.reported_issues = [
            {"issue": "Broken link on Company A profile", "status": "Unresolved"},
            {"issue": "Outdated information on Company B", "status": "Unresolved"}
        ]

        # Show default view (Dashboard)
        self.show_dashboard()

    def change_appearance_mode(self, mode):
        ctk.set_appearance_mode(mode)

    def nav_button_click(self, view_name):
        if view_name == "Dashboard":
            self.show_dashboard()
        elif view_name == "Companies":
            self.show_companies()
        elif view_name == "Users":
            self.show_users()
        elif view_name == "Issues":
            self.show_issues()
        elif view_name == "Settings":
            self.show_settings()

    def clear_main_frame(self):
        # Destroy all widgets in the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_main_frame()

        # Dashboard Header
        header = ctk.CTkLabel(
            self.main_frame,
            text="Dashboard",
            font=ctk.CTkFont(size=24, weight="bold"),
            fg_color="transparent",
            text_color=self.text_color
        )
        header.pack(pady=20, padx=20, anchor="w")

        # Add dashboard widgets here (e.g., statistics, charts)

    def show_companies(self):
        self.clear_main_frame()

        # Companies Header
        header = ctk.CTkLabel(
            self.main_frame,
            text="Company Management",
            font=ctk.CTkFont(size=24, weight="bold"),
            fg_color="transparent",
            text_color=self.text_color
        )
        header.pack(pady=20, padx=20, anchor="w")

        # Add Company Frame
        add_company_frame = ctk.CTkFrame(self.main_frame)
        add_company_frame.pack(fill="x", padx=20, pady=10)

        # Company Input Fields
        name_entry = ctk.CTkEntry(add_company_frame, placeholder_text="Company Name")
        name_entry.pack(side="left", padx=10, pady=10)

        location_entry = ctk.CTkEntry(add_company_frame, placeholder_text="Location")
        location_entry.pack(side="left", padx=10, pady=10)

        add_button = ctk.CTkButton(
            add_company_frame,
            text="Add Company",
            command=lambda: self.add_company(name_entry, location_entry)
        )
        add_button.pack(side="left", padx=10, pady=10)

        # Companies Table
        table_frame = ctk.CTkFrame(self.main_frame)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Create Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="#2b2b2b",
            foreground="white",
            fieldbackground="#2b2b2b",
            borderwidth=0,
            highlightthickness=0
        )
        style.configure("Treeview.Heading", background=self.primary_color, foreground="white")
        style.map("Treeview", background=[('selected', self.accent_color)])

        columns = ("ID", "Name", "Location")
        self.company_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Treeview"
        )

        # Configure columns
        for col in columns:
            self.company_table.heading(col, text=col)
            self.company_table.column(col, anchor="center", width=150)

        self.update_companies_table()

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.company_table.yview)
        self.company_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.company_table.pack(fill="both", expand=True)

    def add_company(self, name_entry, location_entry):
        name = name_entry.get()
        location = location_entry.get()

        if name and location:
            self.companies.append({"name": name, "location": location})
            name_entry.delete(0, 'end')
            location_entry.delete(0, 'end')
            self.update_companies_table()
        else:
            messagebox.showwarning("Input Error", "Please enter both Company Name and Location.")

    def update_companies_table(self):
        # Clear existing items
        for item in self.company_table.get_children():
            self.company_table.delete(item)

        # Insert companies
        for i, company in enumerate(self.companies, 1):
            self.company_table.insert(
                "",
                "end",
                values=(i, company["name"], company["location"])
            )

    def show_users(self):
        self.clear_main_frame()

        # Users Header
        header = ctk.CTkLabel(
            self.main_frame,
            text="User Management",
            font=ctk.CTkFont(size=24, weight="bold"),
            fg_color="transparent",
            text_color=self.text_color
        )
        header.pack(pady=20, padx=20, anchor="w")

        # Add User Frame
        add_user_frame = ctk.CTkFrame(self.main_frame)
        add_user_frame.pack(fill="x", padx=20, pady=10)

        # User Input Fields
        username_entry = ctk.CTkEntry(add_user_frame, placeholder_text="Username")
        username_entry.pack(side="left", padx=10, pady=10)

        role_entry = ctk.CTkEntry(add_user_frame, placeholder_text="Role")
        role_entry.pack(side="left", padx=10, pady=10)

        add_button = ctk.CTkButton(
            add_user_frame,
            text="Add User",
            command=lambda: self.add_user(username_entry, role_entry)
        )
        add_button.pack(side="left", padx=10, pady=10)

        # Users Table
        table_frame = ctk.CTkFrame(self.main_frame)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Create Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="#2b2b2b",
            foreground="white",
            fieldbackground="#2b2b2b",
            borderwidth=0,
            highlightthickness=0
        )
        style.configure("Treeview.Heading", background=self.primary_color, foreground="white")
        style.map("Treeview", background=[('selected', self.accent_color)])

        columns = ("ID", "Username", "Role", "Status", "Actions")
        self.user_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Treeview"
        )

        # Configure columns
        for col in columns:
            self.user_table.heading(col, text=col)
            if col == "Actions":
                self.user_table.column(col, anchor="center", width=100)
            else:
                self.user_table.column(col, anchor="center", width=150)

        self.update_users_table()

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.user_table.yview)
        self.user_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.user_table.pack(fill="both", expand=True)

        # Bind double-click to delete user
        self.user_table.bind("<Double-1>", self.on_user_double_click)

    def add_user(self, username_entry, role_entry):
        username = username_entry.get()
        role = role_entry.get()

        if username and role:
            self.users.append({"username": username, "role": role, "status": "Active"})
            username_entry.delete(0, 'end')
            role_entry.delete(0, 'end')
            self.update_users_table()
        else:
            messagebox.showwarning("Input Error", "Please enter both Username and Role.")

    def update_users_table(self):
        # Clear existing items
        for item in self.user_table.get_children():
            self.user_table.delete(item)

        # Insert users
        for i, user in enumerate(self.users, 1):
            self.user_table.insert(
                "",
                "end",
                values=(i, user["username"], user["role"], user["status"], "Delete")
            )

    def on_user_double_click(self, event):
        item = self.user_table.selection()
        if item:
            user_id = self.user_table.item(item, "values")[0]
            user = self.users[int(user_id) - 1]
            confirm = messagebox.askyesno("Delete User", f"Are you sure you want to delete user '{user['username']}'?")
            if confirm:
                del self.users[int(user_id) - 1]
                self.update_users_table()

    def show_issues(self):
        self.clear_main_frame()

        # Issues Header
        header = ctk.CTkLabel(
            self.main_frame,
            text="Reported Issues",
            font=ctk.CTkFont(size=24, weight="bold"),
            fg_color="transparent",
            text_color=self.text_color
        )
        header.pack(pady=20, padx=20, anchor="w")

        # Issues Table
        table_frame = ctk.CTkFrame(self.main_frame)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Create Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="#2b2b2b",
            foreground="white",
            fieldbackground="#2b2b2b",
            borderwidth=0,
            highlightthickness=0
        )
        style.configure("Treeview.Heading", background=self.primary_color, foreground="white")
        style.map("Treeview", background=[('selected', self.accent_color)])

        columns = ("ID", "Issue", "Status")
        self.issues_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Treeview"
        )

        # Configure columns
        for col in columns:
            self.issues_table.heading(col, text=col)
            self.issues_table.column(col, anchor="center", width=200)

        self.update_issues_table()

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.issues_table.yview)
        self.issues_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.issues_table.pack(fill="both", expand=True)

    def update_issues_table(self):
        # Clear existing items
        for item in self.issues_table.get_children():
            self.issues_table.delete(item)

        # Insert issues
        for i, issue in enumerate(self.reported_issues, 1):
            self.issues_table.insert(
                "",
                "end",
                values=(i, issue["issue"], issue["status"])
            )

    def show_settings(self):
        self.clear_main_frame()

        # Settings Header
        header = ctk.CTkLabel(
            self.main_frame,
            text="Settings",
            font=ctk.CTkFont(size=24, weight="bold"),
            fg_color="transparent",
            text_color=self.text_color
        )
        header.pack(pady=20, padx=20, anchor="w")

        # Settings Options (Add settings widgets as needed)
        settings_label = ctk.CTkLabel(
            self.main_frame,
            text="Settings can be configured here.",
            font=ctk.CTkFont(size=16),
            fg_color="transparent",
            text_color=self.text_color
        )
        settings_label.pack(pady=10, padx=20, anchor="w")

        # Example: Toggle Switch
        toggle = ctk.CTkSwitch(
            self.main_frame,
            text="Enable Notifications",
            command=lambda: messagebox.showinfo("Toggle", "Notifications Toggled")
        )
        toggle.pack(pady=10, padx=20, anchor="w")

        # Example: Dark Mode Toggle
        dark_mode_toggle = ctk.CTkSwitch(
            self.main_frame,
            text="Dark Mode",
            command=lambda: self.change_appearance_mode("dark" if dark_mode_toggle.get() else "light")
        )
        dark_mode_toggle.set(ctk.get_appearance_mode() == "dark")
        dark_mode_toggle.pack(pady=10, padx=20, anchor="w")


if __name__ == "__main__":
    app = AdminPanel()
    app.mainloop()
