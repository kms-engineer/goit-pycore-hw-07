import re
from field import Field

class Birthday(Field):

    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)

    @staticmethod
    def validate(birthday: str) -> bool:
        return bool(re.match(r"\d{2}\.\d{2}\.\d{4}", birthday))