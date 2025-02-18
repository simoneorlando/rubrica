import tkinter as tk
from tkinter import ttk
from application.view_controller import ViewController
from storage.contact_storage import ContactStorage


def __launch_ui__(storage: ContactStorage):
    root = tk.Tk()
    root.title("Turing Rubrica")
    root.geometry("1200x500")

    # Configure global styles
    style = ttk.Style()
    style.configure(
        "Treeview", rowheight=30, font=("Arial", 12)
    )  # Larger row height & text
    style.configure(
        "Treeview.Heading", font=("Arial", 14, "bold")
    )  # Larger header text
    style.configure("TButton", font=("Arial", 12))  # Standard button font
    style.configure("TLabel", font=("Arial", 12))  # Standard label font
    style.configure("TEntry", font=("Arial", 12))  # Standard entry font

    # Contact List
    columns = ("Name", "Surname", "Phone", "Address", "Age")

    treeview_contacts = ttk.Treeview(root, columns=columns, show="headings", height=10)
    treeview_contacts.pack(pady=10, fill=tk.BOTH, expand=True)

    # Define column headings
    for col in columns:
        treeview_contacts.heading(col, text=col)
        treeview_contacts.column(col, anchor=tk.CENTER, width=120)

    # Initialize ViewController
    vc = ViewController(root, storage, treeview_contacts)

    # Buttons
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=5)

    btn_add = tk.Button(btn_frame, text="New", command=vc.open_add_window, width=12)
    btn_add.grid(row=0, column=0, padx=5)

    btn_edit = tk.Button(btn_frame, text="Edit", command=vc.open_edit_window, width=12)
    btn_edit.grid(row=0, column=1, padx=5)

    btn_delete = tk.Button(
        btn_frame, text="Delete", command=vc.delete_contact, width=12
    )
    btn_delete.grid(row=0, column=2, padx=5)

    # Populate contacts at startup
    vc.display_contacts()

    # Run main loop
    root.mainloop()
