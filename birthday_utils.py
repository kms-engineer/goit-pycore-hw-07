from datetime import datetime, timedelta, date

def get_birthday_for_year(orig_birthday: date, target_year: int) -> date:
    month = orig_birthday.month
    day = orig_birthday.day

    if month == 2 and day == 29 and not is_leap_year(target_year):
        month = 3
        day = 1

    return datetime(target_year, month, day).date()

def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def move_to_monday_if_weekend(input_date: date) -> date:
    weekday = input_date.weekday()
    if weekday == 5:
        return input_date + timedelta(days=2)
    elif weekday == 6:
        return input_date + timedelta(days=1)
    else:
        return input_date