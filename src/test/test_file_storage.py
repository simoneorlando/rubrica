import os.path
from models.contact import Contact
from typing import List
from storage.file_storage import FileStorage


def read_file_lines(file_path: str) -> List:
    with open(file_path, "r") as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]


def test_file_storage():
    test_file_storage_name = "test.txt"
    if os.path.exists(test_file_storage_name):
        os.remove(test_file_storage_name)
    storage = FileStorage(test_file_storage_name)

    assert len(storage.contacts) == 0

    contact = Contact("Mario", "Rossi", "3999999", "Via Cupertino", 19)
    assert storage.add_contact(contact)

    assert len(storage.contacts) == 1

    assert os.path.exists(test_file_storage_name)
    file_lines = read_file_lines(test_file_storage_name)
    assert len(file_lines) == 1

    line = file_lines[0]
    contact_info = line.split(";")

    assert len(contact_info) == 5
    assert contact_info[0] == "Mario"
    assert contact_info[1] == "Rossi"
    assert contact_info[2] == "3999999"
    assert contact_info[3] == "Via Cupertino"
    assert contact_info[4] == "19"

    contact = Contact("Mario", "Verdi", "3999999", "Via Cupertino", 19, contact.id)

    assert storage.update_contact(contact)

    assert len(storage.contacts) == 1

    file_lines = read_file_lines(test_file_storage_name)
    assert len(file_lines) == 1
    line = file_lines[0]
    contact_info = line.split(";")

    assert len(contact_info) == 5
    assert contact_info[0] == "Mario"
    assert contact_info[1] == "Verdi"
    assert contact_info[2] == "3999999"
    assert contact_info[3] == "Via Cupertino"
    assert contact_info[4] == "19"

    contact2 = Contact("Giuseppe", "Verdi", "77777777", "Via Cupertino", 25)
    assert storage.add_contact(contact2)

    assert len(storage.contacts) == 2

    file_lines = read_file_lines(test_file_storage_name)
    assert len(file_lines) == 2

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

    file_lines = read_file_lines(test_file_storage_name)
    assert len(file_lines) == 1

    os.remove(test_file_storage_name)
