import re
from datetime import datetime


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_phone(phone):
    pattern = r'^\+?1?\d{9,15}$'
    return re.match(pattern, phone) is not None


def validate_date(date_str):
    format_date = '%Y-%m-%d'
    try:
        datetime.strptime(date_str, format_date)
        return True
    except ValueError:
        return False