import os
from models.contact import Contact
from storage.sql_database import DatabaseStorage


def test_sql_database():
    test_file_storage_name = "test.db"
    if os.path.exists(test_file_storage_name):
        os.remove(test_file_storage_name)
    storage = DatabaseStorage(test_file_storage_name)

    assert len(storage.contacts) == 0

    contact = Contact("Mario", "Rossi", "3999999", "Via Cupertino", 19)
    assert storage.add_contact(contact)

    assert len(storage.contacts) == 1

    assert os.path.exists(test_file_storage_name)

    contact = Contact("Mario", "Verdi", "3999999", "Via Cupertino", 19, contact.id)

    assert storage.update_contact(contact)

    assert len(storage.contacts) == 1

    contact2 = Contact("Giuseppe", "Verdi", "77777777", "Via Cupertino", 25)
    assert storage.add_contact(contact2)

    assert len(storage.contacts) == 2

    contact_dict = storage.contacts
    assert contact_dict
    assert len(contact_dict) == 2

    query = "Giuseppe"
    result = storage.search_contacts(query)
    assert result
    assert len(result) == 1

    assert result[0].name == query

    query = "777"
    result = storage.search_contacts(query)
    assert result
    assert len(result) == 1

    assert result[0].name == "Giuseppe"

    assert storage.delete_contact(contact2.id)
    assert len(storage.contacts) == 1

    os.remove(test_file_storage_name)
