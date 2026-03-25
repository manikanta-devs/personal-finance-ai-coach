import calendar
from datetime import date


def calculate_age(date_of_birth):
    """
    Calculate the current age in years based on date of birth.

    Parameters:
    date_of_birth (date): The date of birth as a datetime.date object.

    Returns:
    int: The current age in years.
    """
    today = date.today()
    age = today.year - date_of_birth.year
    if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
        age -= 1
    return age


def years_to_retirement(date_of_birth, retirement_age=65):
    """
    Calculate the number of years remaining until retirement.

    Parameters:
    date_of_birth (date): The date of birth as a datetime.date object.
    retirement_age (int): The target retirement age (default is 65).

    Returns:
    int: The number of years remaining until retirement.
         Returns 0 if the person has already reached retirement age.
    """
    current_age = calculate_age(date_of_birth)
    remaining = retirement_age - current_age
    return max(0, remaining)


def retirement_date(date_of_birth, retirement_age=65):
    """
    Calculate the expected retirement date.

    Parameters:
    date_of_birth (date): The date of birth as a datetime.date object.
    retirement_age (int): The target retirement age (default is 65).

    Returns:
    date: The expected retirement date.
    """
    retirement_year = date_of_birth.year + retirement_age
    try:
        return date(retirement_year, date_of_birth.month, date_of_birth.day)
    except ValueError:
        # Handle Feb 29 birthdays: use Feb 29 if retirement year is a leap year,
        # otherwise fall back to Feb 28.
        day = 29 if calendar.isleap(retirement_year) else 28
        return date(retirement_year, date_of_birth.month, day)
