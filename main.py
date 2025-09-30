from typing import List, Tuple
from record import Record
from address_book import AddressBook

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Contact not found: {e}"
        except ValueError as e:
            return f"Error: {e}"
        except IndexError as e:
            return f"Error: {e}"
        except Exception as e:
            return f"An error occurred: {type(e).__name__}: {e}"
    return inner

def parse_input(user_input: str) -> Tuple[str, List[str]]:
    args = user_input.split()
    if not args:
        return "", []
    command = args[0].lower()
    return command, args[1:]

@input_error
def add_contact(args: List[str], book: AddressBook) -> str:
    if len(args) < 2:
        raise ValueError("Add command requires 2 arguments: name and phone")

    name, phone = args[0], args[1]

    try:
        record = book.find(name)
        record.add_phone(phone)
        message = "Contact updated."
    except KeyError:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        message = "Contact added."

    return message

@input_error
def change_contact(args: List[str], book: AddressBook) -> str:
    if len(args) < 3:
        raise ValueError("Change command requires 3 arguments: name, old phone, and new phone")

    name, old_phone, new_phone = args[0], args[1], args[2]

    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return "Contact phone number updated."

@input_error
def show_phone(args: List[str], book: AddressBook) -> str:
    if len(args) < 1:
        raise ValueError("Phone command requires 1 argument: name")

    name = args[0]
    record = book.find(name)

    if not record.phones:
        return f"{name} has no phone numbers."

    phones = "; ".join(phone.value for phone in record.phones)
    return f"{name}: {phones}"

@input_error
def show_all(args: List[str], book: AddressBook) -> str:
    if not book.data:
        return "No contacts found."

    lines = ["All contacts:"]
    for record in book.data.values():
        lines.append(str(record))
    return "\n".join(lines)

@input_error
def add_birthday(args: List[str], book: AddressBook) -> str:
    if len(args) < 2:
        raise ValueError("Add-birthday command requires 2 arguments: name and birthday (DD.MM.YYYY)")

    name, birthday = args[0], args[1]

    record = book.find(name)
    record.add_birthday(birthday)
    return f"Birthday added for {name}."

@input_error
def show_birthday(args: List[str], book: AddressBook) -> str:
    if len(args) < 1:
        raise ValueError("Show-birthday command requires 1 argument: name")

    name = args[0]
    record = book.find(name)

    if record.birthday:
        return f"{name}'s birthday: {record.birthday}"
    else:
        return f"No birthday set for {name}."

@input_error
def birthdays(args: List[str], book: AddressBook) -> str:
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays in the next 7 days."

    lines = ["Upcoming birthdays:"]
    for contact in upcoming:
        lines.append(f"{contact['name']}: {contact['congratulation_date']}")
    return "\n".join(lines)

def hello(args: List[str], book: AddressBook) -> str:
    return "How can I help you?"

COMMANDS = {
    "hello": hello,
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone,
    "all": show_all,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": birthdays,
}

@input_error
def process_command(user_input: str, book: AddressBook) -> str:
    command, args = parse_input(user_input)
    if command in ("close", "exit"):
        return "exit"
    if command in COMMANDS:
        return COMMANDS[command](args, book)
    available = ', '.join(sorted([*COMMANDS.keys(), 'close', 'exit']))
    return f"Invalid command. Available commands: {available}"

def main() -> None:
    book = AddressBook()
    print("Welcome to the assistant bot!\n"
          "Available commands:\n"
          "  hello                            - Show greeting\n"
          "  add <name> <phone>               - Add new contact\n"
          "  change <name> <old> <new>        - Update contact's phone\n"
          "  phone <name>                     - Show contact's phone number(s)\n"
          "  all                              - Show all contacts\n"
          "  add-birthday <name> <DD.MM.YYYY> - Add birthday to contact\n"
          "  show-birthday <name>             - Show contact's birthday\n"
          "  birthdays                        - Show upcoming birthdays\n"
          "  close, exit                      - Exit the bot\n")

    while True:
        try:
            user_input = input("Enter a command: ").strip()
            if not user_input:
                continue
            result = process_command(user_input, book)
            if result == "exit":
                print("Good bye!")
                break
            print(result)
        except KeyboardInterrupt:
            print("\nGood bye!")
            break

if __name__ == "__main__":
    main()

