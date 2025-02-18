import uuid


class Contact:
    def __init__(
        self,
        name: str,
        surname: str,
        phone: str,
        address: str,
        age: int,
        contact_id=None,
    ):
        if contact_id is not None:
            self.id = contact_id
        else:
            self.id = str(uuid.uuid4())  # Generate a unique ID
        self.name = name
        self.surname = surname
        self.phone = phone
        self.address = address
        self.age = int(age)


def validate_age(age):
    """Ensure age is a valid integer > 0 and < 130."""
    try:
        age = int(age)
        return 0 < age < 130
    except ValueError:
        return False
