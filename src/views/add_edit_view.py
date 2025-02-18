import tkinter as tk
from tkinter import ttk

from models.contact import validate_age


class AddEditContactWindow:
    def __init__(self, parent, view_controller, contact=None):
        self.window = tk.Toplevel(parent)
        self.window.title("Edit Contact" if contact else "Add Contact")
        self.window.geometry("600x700")

        # Use the same styles as the main window
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12))
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TEntry", font=("Arial", 12))

        self.vc = view_controller
        self.contact = contact

        # Name
        ttk.Label(self.window, text="Name:").pack(pady=2)
        self.entry_name = ttk.Entry(self.window)
        self.entry_name.pack(pady=2, fill=tk.X, padx=20)
        self.label_name_error = ttk.Label(self.window, text="", foreground="red")
        self.label_name_error.pack()

        # Surname
        ttk.Label(self.window, text="Surname:").pack(pady=2)
        self.entry_surname = ttk.Entry(self.window)
        self.entry_surname.pack(pady=2, fill=tk.X, padx=20)
        self.label_surname_error = ttk.Label(self.window, text="", foreground="red")
        self.label_surname_error.pack()

        # Phone
        ttk.Label(self.window, text="Phone:").pack(pady=2)
        self.entry_phone = ttk.Entry(self.window)
        self.entry_phone.pack(pady=2, fill=tk.X, padx=20)
        self.label_phone_error = ttk.Label(self.window, text="", foreground="red")
        self.label_phone_error.pack()

        # Address
        ttk.Label(self.window, text="Address:").pack(pady=2)
        self.entry_address = ttk.Entry(self.window)
        self.entry_address.pack(pady=2, fill=tk.X, padx=20)
        self.label_address_error = ttk.Label(self.window, text="", foreground="red")
        self.label_address_error.pack()

        # Age
        ttk.Label(self.window, text="Age:").pack(pady=2)
        self.entry_age = ttk.Entry(self.window)
        self.entry_age.pack(pady=2, fill=tk.X, padx=20)
        self.label_age_error = ttk.Label(self.window, text="", foreground="red")
        self.label_age_error.pack()

        # Pre-fill fields if editing
        if contact:
            self.entry_name.insert(0, contact.name)
            self.entry_surname.insert(0, contact.surname)
            self.entry_phone.insert(0, contact.phone)
            self.entry_address.insert(0, contact.address)
            self.entry_age.insert(0, str(contact.age))

        # Buttons
        btn_frame = tk.Frame(self.window)
        btn_frame.pack(pady=15)

        btn_save = ttk.Button(
            btn_frame, text="Save", command=self.save_contact, width=12
        )
        btn_save.grid(row=0, column=0, padx=10)

        btn_cancel = ttk.Button(
            btn_frame, text="Cancel", command=self.window.destroy, width=12
        )
        btn_cancel.grid(row=0, column=1, padx=10)

    def clear_errors(self):
        """Clear all error messages before re-validating."""
        self.label_name_error.config(text="")
        self.label_surname_error.config(text="")
        self.label_phone_error.config(text="")
        self.label_address_error.config(text="")
        self.label_age_error.config(text="")

    def save_contact(self):
        """Save new or edited contact"""
        self.clear_errors()  # Clear previous error messages

        name = self.entry_name.get()
        surname = self.entry_surname.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get()
        age = self.entry_age.get()

        valid = True  # Flag to check if all inputs are valid

        # Check if all fields are filled
        if not name:
            self.label_name_error.config(text="Name cannot be empty")
            valid = False

        if not surname:
            self.label_surname_error.config(text="Surname cannot be empty")
            valid = False

        if not phone:
            self.label_phone_error.config(text="Phone number is required")
            valid = False

        if not address:
            self.label_address_error.config(text="Address is required")
            valid = False

        if not validate_age(age):
            self.label_age_error.config(text="Invalid age")
            valid = False

        if not valid:
            return  # Stop execution if any validation fails

        if self.contact:
            self.vc.update_contact(
                self.contact.id, name, surname, phone, address, int(age)
            )
        else:
            self.vc.add_contact(name, surname, phone, address, int(age))

        self.window.destroy()
