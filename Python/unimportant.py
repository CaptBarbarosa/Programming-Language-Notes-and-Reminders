import tkinter as tk
from tkinter import messagebox, ttk

# Initialize the main window
root = tk.Tk()
root.title("Admin Panel")
root.geometry("700x500")
root.config(bg="#F7F7F7")  # Light grey background

# Data for companies and reported issues
companies = [{"name": "Company A", "location": "Location A"},
             {"name": "Company B", "location": "Location B"}]

reported_issues = [{"issue": "Broken link on Company A profile", "status": "Unresolved"},
                   {"issue": "Outdated information on Company B", "status": "Unresolved"}]

# Function to update the companies list
def update_companies_list():
    for i in company_table.get_children():
        company_table.delete(i)  # Clear table
    for index, company in enumerate(companies):
        company_table.insert("", "end", values=(index + 1, company['name'], company['location']))

# Function to delete a company
def delete_company():
    selected = company_table.selection()
    if selected:
        for i in selected:
            values = company_table.item(i, "values")
            del companies[int(values[0]) - 1]
            update_companies_list()

# Function to add a new company
def add_company():
    name = name_entry.get()
    location = location_entry.get()
    if name and location:
        companies.append({"name": name, "location": location})
        update_companies_list()
        name_entry.delete(0, tk.END)
        location_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Company added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please enter both name and location.")

# Function to update the issues list
def update_issues_list():
    issue_list.delete(0, tk.END)
    for index, issue in enumerate(reported_issues):
        status_text = f"{index + 1}. {issue['issue']} - {issue['status']}"
        issue_list.insert(tk.END, status_text)

# Function to resolve an issue
def resolve_issue():
    selected = issue_list.curselection()
    if selected:
        index = selected[0]
        reported_issues[index]["status"] = "Resolved"
        update_issues_list()
        check_notifications()

# Function to check if there are unresolved issues and update the notification label
def check_notifications():
    unresolved_issues = any(issue['status'] == "Unresolved" for issue in reported_issues)
    if unresolved_issues:
        notification_label.config(text="Unresolved Issues!", fg="red")
    else:
        notification_label.config(text="All issues resolved.", fg="green")

# Title Label
title_label = tk.Label(root, text="Admin Panel", font=("Arial", 20, "bold"), fg="#6200EE", bg="#F7F7F7")
title_label.pack(pady=10)

# Frame for clickable links (Add/Manage Users, Manage Companies, View/Resolve Issues)
link_frame = tk.Frame(root, bg="#F7F7F7")
link_frame.pack(pady=10)

# Clickable Links (Simulating Features)
users_label = tk.Label(link_frame, text="Manage Users", fg="#6200EE", bg="#F7F7F7", font=("Arial", 12, "underline"))
companies_label = tk.Label(link_frame, text="Manage Companies", fg="#6200EE", bg="#F7F7F7", font=("Arial", 12, "underline"))
problems_label = tk.Label(link_frame, text="Reported Issues", fg="#6200EE", bg="#F7F7F7", font=("Arial", 12, "underline"))

# Arrange clickable links
users_label.grid(row=0, column=0, padx=10)
companies_label.grid(row=0, column=1, padx=10)
problems_label.grid(row=0, column=2, padx=10)

# Frame for companies management
company_frame = tk.Frame(root, bg="#F7F7F7")
company_frame.pack(pady=10, fill="x", padx=20)

# Table for displaying companies
company_table = ttk.Treeview(company_frame, columns=("ID", "Name", "Location"), show="headings", height=6)
company_table.heading("ID", text="ID")
company_table.heading("Name", text="Name")
company_table.heading("Location", text="Location")
company_table.column("ID", width=30, anchor="center")
company_table.column("Name", width=150, anchor="w")
company_table.column("Location", width=250, anchor="w")
company_table.pack(side="left", fill="x")

# Scrollbar for the companies table
scrollbar = ttk.Scrollbar(company_frame, orient="vertical", command=company_table.yview)
company_table.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Button to delete selected company
delete_company_button = tk.Button(root, text="Delete Company", bg="#FF0000", fg="white", command=delete_company)
delete_company_button.pack(pady=10)

# Divider line
divider = ttk.Separator(root, orient="horizontal")
divider.pack(fill="x", padx=20, pady=10)

# Frame for the Add Company section
add_company_frame = tk.Frame(root, bg="#F7F7F7")
add_company_frame.pack(pady=20, fill="x", padx=20)

# Add Company Inputs
name_label = tk.Label(add_company_frame, text="Company Name:", bg="#F7F7F7", font=("Arial", 12))
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(add_company_frame, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

location_label = tk.Label(add_company_frame, text="Location:", bg="#F7F7F7", font=("Arial", 12))
location_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
location_entry = tk.Entry(add_company_frame, width=30)
location_entry.grid(row=1, column=1, padx=10, pady=5)

# Add Company Button
add_company_button = tk.Button(add_company_frame, text="Add Company", bg="#6200EE", fg="white", width=20, command=add_company)
add_company_button.grid(row=2, column=1, pady=10)

# Divider line
divider = ttk.Separator(root, orient="horizontal")
divider.pack(fill="x", padx=20, pady=10)

# Notification label for unresolved issues
notification_label = tk.Label(root, text="", bg="#F7F7F7", font=("Arial", 12))
notification_label.pack()

# Frame for issue management
issue_frame = tk.Frame(root, bg="#F7F7F7")
issue_frame.pack(pady=10, fill="both", expand=True)

# Listbox for displaying reported issues
issue_list = tk.Listbox(issue_frame, height=6, font=("Arial", 12))
issue_list.pack(pady=10, fill="both", expand=True)

# Button to resolve selected issue
resolve_issue_button = tk.Button(root, text="Resolve Issue", bg="#6200EE", fg="white", command=resolve_issue)
resolve_issue_button.pack(pady=10)

# Initial population of companies and issues lists
update_companies_list()
update_issues_list()
check_notifications()

# Start the Tkinter event loop
root.mainloop()
