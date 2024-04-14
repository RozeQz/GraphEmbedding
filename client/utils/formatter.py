from datetime import datetime


def format_number(num):
    if num.is_integer():
        return int(num)
    else:
        return num


def format_date(date):
    return datetime.fromisoformat(date).strftime("%Y-%m-%d %H:%M:%S")
