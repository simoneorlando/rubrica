from models.contact import Contact
from typing import List, Dict


class ContactController:
    def __init__(self, storage):
        self.storage = storage  # Dependency Injection of Storage

    def add_contact(self, name, surname, phone, address, age) -> bool:
        new_contact = Contact(name, surname, phone, address, age)
        return self.storage.add_contact(new_contact)

    def get_all_contacts(self) -> Dict:
        return self.storage.contacts

    def search_contacts(self, query) -> List:
        return self.storage.search_contacts(query)

    def delete_contact(self, contact_id) -> bool:
        return self.storage.delete_contact(contact_id)

    def update_contact(self, contact_id, name, surname, phone, address, age) -> bool:
        """Updates an existing contact by replacing the old details with new ones."""
        updated_contact = Contact(name, surname, phone, address, age, contact_id)
        return self.storage.update_contact(updated_contact)
