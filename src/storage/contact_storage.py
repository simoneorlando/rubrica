from abc import ABC, abstractmethod
from models.contact import Contact


class ContactStorage(ABC):
    @abstractmethod
    def add_contact(self, contact: Contact):
        pass

    @abstractmethod
    def update_contact(self, contact: Contact):
        pass

    @abstractmethod
    def search_contacts(self, query):
        pass

    @abstractmethod
    def delete_contact(self, contact_id):
        pass
