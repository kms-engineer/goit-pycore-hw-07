import re
from field import Field

class Phone(Field):
    def __init__(self, raw: str):
        digits = self.normalize(raw)
        if not self.validate(digits):
            raise ValueError(
                f"Invalid phone number: '{raw}'. Expected exactly 10 digits after normalization."
            )
        super().__init__(digits)

    @staticmethod
    def validate(phone: str) -> bool:
        return phone.isdigit() and len(phone) == 10

    @staticmethod
    def normalize(raw: str) -> str:
        return re.sub(r"\D+", "", raw)