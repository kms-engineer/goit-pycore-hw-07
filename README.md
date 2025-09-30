# Command line Assistant Bot

A command-line assistant for managing contacts and birthdays.

## Quick Start

```bash
python3 main.py
```

## Available Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `add` | `add <name> <phone>` | Add new contact or phone to existing contact |
| `change` | `change <name> <old_phone> <new_phone>` | Update contact's phone number |
| `phone` | `phone <name>` | Show contact's phone number(s) |
| `all` | `all` | Show all contacts |
| `add-birthday` | `add-birthday <name> <DD.MM.YYYY>` | Add birthday to contact |
| `show-birthday` | `show-birthday <name>` | Show contact's birthday |
| `birthdays` | `birthdays` | Show upcoming birthdays (next 7 days) |
| `hello` | `hello` | Show greeting |
| `close/exit` | `close` or `exit` | Exit the bot |

## Phone Number Format

- Accepts various formats: `1234567890`, `(123) 456-7890`, `123-456-7890`
- Automatically normalizes to 10 digits
- Validates exactly 10 digits after normalization

## Birthday Format

- Required format: `DD.MM.YYYY` (e.g., `25.12.1990`)
- Handles leap years correctly
- Weekend birthdays moved to following Monday for celebrations