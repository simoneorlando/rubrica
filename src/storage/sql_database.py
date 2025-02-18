import sqlite3
from storage.contact_storage import ContactStorage
from models.contact import Contact
from typing import List


class DatabaseStorage(ContactStorage):
    def __init__(self, db_name="address_book.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
        self.contacts = self.__read_data()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS contacts (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                address TEXT NOT NULL,
                age INTEGER
            )
        """
        )
        self.conn.commit()

    def add_contact(self, contact: Contact) -> bool:
        """Add a new contact to the db."""
        try:
            self.cursor.execute(
                "INSERT INTO contacts VALUES (?, ?, ?, ?, ?, ?)",
                (
                    contact.id,
                    contact.name,
                    contact.surname,
                    contact.phone,
                    contact.address,
                    contact.age,
                ),
            )
            self.conn.commit()
            self.contacts = self.__read_data()
            return True
        except sqlite3.IntegrityError:
            return False

    def update_contact(self, contact: Contact) -> bool:
        """Update an existing contact."""
        try:
            self.cursor.execute(
                """
                UPDATE contacts
                SET name = ?, surname = ?, phone = ?, address = ?, age = ?
                WHERE id = ?
            """,
                (
                    contact.name,
                    contact.surname,
                    contact.phone,
                    contact.address,
                    contact.age,
                    contact.id,
                ),
            )
            self.conn.commit()
            self.contacts = self.__read_data()
            return True
        except sqlite3.IntegrityError:
            return False

    def search_contacts(self, query) -> List:
        """Search for contacts by name or phone number."""
        self.cursor.execute(
            "SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?",
            (f"%{query}%", f"%{query}%"),
        )
        result = []
        for row in self.cursor.fetchall():
            contact_id, name, surname, phone, address, age = row
            result.append(Contact(name, surname, phone, address, age, contact_id))
        return result

    def delete_contact(self, contact_id) -> bool:
        """Delete a contact by id."""
        try:
            self.cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
            self.conn.commit()
            self.contacts = self.__read_data()
            return True
        except sqlite3.IntegrityError:
            return False

    def __read_data(self):
        """Return all contacts from the db."""
        self.cursor.execute("SELECT * FROM contacts")
        result = {}
        for row in self.cursor.fetchall():
            contact_id, name, surname, phone, address, age = row
            result[contact_id] = Contact(name, surname, phone, address, age, contact_id)
        return result
