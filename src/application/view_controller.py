from tkinter import messagebox
from application.contact_controller import ContactController
from views.add_edit_view import AddEditContactWindow


class ViewController:
    def __init__(self, root, storage, treeview):
        self.root = root
        self.treeview = treeview
        self.controller = ContactController(storage)

        self.display_contacts()

    def display_contacts(self):
        """Show contacts in the treeview."""
        # Clear existing rows
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Insert all contacts into treeview
        for contact in self.controller.get_all_contacts().values():
            self.treeview.insert(
                "",
                "end",
                values=(
                    contact.name,
                    contact.surname,
                    contact.phone,
                    contact.address,
                    contact.age,
                ),
            )

    def open_add_window(self):
        """Open window to add a new contact."""
        AddEditContactWindow(self.root, self)

    def open_edit_window(self):
        """Open window to edit a selected contact."""
        selected_item = self.treeview.selection()
        if not selected_item:
            messagebox.showerror("Error", "A contact must be selected")
            return

        contact_text = self.treeview.item(selected_item)["values"]
        phone = str(contact_text[2])  # Extract phone number from the selected row

        contacts = self.controller.search_contacts(phone)
        if contacts:
            AddEditContactWindow(self.root, self, contacts[0])

    def add_contact(self, name, surname, phone, address, age):
        """Add a new contact via the controller."""
        if self.controller.add_contact(name, surname, phone, address, age):
            self.display_contacts()
        else:
            messagebox.showerror("Error", "An error occurred!")

    def update_contact(self, contact_id, name, surname, phone, address, age):
        """Update an existing contact."""
        if self.controller.update_contact(
            contact_id, name, surname, phone, address, age
        ):
            self.display_contacts()
        else:
            messagebox.showerror("Error", "An error occurred!")

    def delete_contact(self):
        """Delete a selected contact after confirmation."""
        selected_item = self.treeview.selection()
        if not selected_item:
            messagebox.showerror("Error", "A contact must be selected")
            return

        contact_values = self.treeview.item(selected_item)["values"]
        name, surname, phone = (
            contact_values[0],
            contact_values[1],
            contact_values[2],
        )  # Extract name, surname, phone

        # Confirmation popup
        confirm = messagebox.askyesno(
            "Confirm Deletion", f'Are you sure you want to delete "{name} {surname}"?'
        )
        if not confirm:
            return  # Do nothing if user selects "No"

        # Find the contact by phone number and delete
        contacts = self.controller.search_contacts(str(phone))
        if contacts:
            contact_to_be_deleted = contacts[0]
            if self.controller.delete_contact(contact_to_be_deleted.id):
                self.display_contacts()
