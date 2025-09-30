import uuid
from name import Name
from phone import Phone
from birthday import Birthday

class Record:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None

    def add_phone(self, phone: str) -> None:
        phone_obj = Phone(phone)
        if phone_obj in self.phones:
            raise ValueError("Phone number already exists")
        self.phones.append(phone_obj)

    def find_phone(self, phone: str) -> Phone:
        norm = Phone.normalize(phone)
        for p in self.phones:
            if p.value == norm:
                return p
        raise ValueError("Phone number not found")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        current = self.find_phone(old_phone)
        new_obj = Phone(new_phone)
        if new_obj in self.phones and new_obj != current:
            raise ValueError("New phone duplicates existing number")
        idx = self.phones.index(current)
        self.phones[idx] = new_obj

    def remove_phone(self, phone: str) -> None:
        p = self.find_phone(phone)
        self.phones.remove(p)

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def __str__(self) -> str:
        phones_str = "; ".join(p.value for p in self.phones) or "—"
        birthday_str = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{birthday_str}"