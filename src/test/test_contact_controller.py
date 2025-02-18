import os
from src.application.contact_controller import ContactController
from src.storage.file_storage import FileStorage


def test_contact_controller_with_file_storage():
    test_file_storage_name = "test.txt"
    if os.path.exists(test_file_storage_name):
        os.remove(test_file_storage_name)
    storage = FileStorage(test_file_storage_name)
    controller = ContactController(storage)

    assert controller.add_contact("Mario", "Verdi", "3999999", "Via Cupertino", 19)

    contacts_dict = controller.get_all_contacts()
    assert len(contacts_dict) == 1

    assert controller.add_contact("Giuseppe", "Verdi", "3999999", "Via Cupertino", 19)

    assert len(contacts_dict) == 2

    query = "Giuseppe"
    result = controller.search_contacts(query)
    assert len(result) == 1
    assert result[0].name == query

    assert controller.update_contact(
        result[0].id, "Giuseppe", "Verdi", "3999999", "Via Cupertino", 35
    )
    result = controller.search_contacts(query)
    assert len(result) == 1
    assert result[0].age == 35

    assert controller.delete_contact(result[0].id)
    result = controller.search_contacts(query)
    assert len(result) == 0

    os.remove(test_file_storage_name)
