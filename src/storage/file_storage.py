import os
from storage.contact_storage import ContactStorage
from typing import Dict, List
from models.contact import Contact


class FileStorage(ContactStorage):
    def __init__(self, file_name="informazioni.txt"):
        self.file_name = file_name
        self.contacts = self.__read_data()

    def add_contact(self, contact: Contact) -> bool:
        """Append a new contact to the text file."""
        try:
            self.contacts[contact.id] = contact
            self.__write_data()
            return True
        except Exception:
            return False

    def update_contact(self, contact: Contact) -> bool:
        """Update an existing contact."""
        try:
            if contact.id not in self.contacts:
                raise KeyError
            self.contacts[contact.id] = contact
            self.__write_data()
            return True
        except Exception:
            return False

    def search_contacts(self, query) -> List:
        """Search for contacts by name or phone number."""
        return [
            contact
            for contact_id, contact in self.contacts.items()
            if query in contact.name or query in contact.phone
        ]

    def delete_contact(self, contact_id) -> bool:
        """Delete a contact by id."""
        try:
            del self.contacts[contact_id]
            self.__write_data()
            return True
        except Exception:
            return False

    def __read_data(self) -> Dict:
        """Return all contacts from the file."""
        contacts = {}
        if not os.path.exists(self.file_name):
            return contacts  # Return empty Dict if file does not exist

        with open(self.file_name, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                parts = line.split(";")
                if len(parts) == 5:  # Ensure all fields are present
                    name, surname, address, phone, age = parts
                    contact = Contact(name, surname, phone, address, int(age))
                    contacts[contact.id] = contact
        return contacts

    def __write_data(self) -> bool:
        """Save all contacts to the text file in the required format."""
        try:
            with open(self.file_name, "w", encoding="utf-8") as file:
                for contact_id, contact in self.contacts.items():
                    file.write(
                        f"{contact.name};{contact.surname};{contact.phone};{contact.address};{contact.age}\n"
                    )
            return True
        except Exception:
            return False
