from datetime import datetime
from calendar import monthrange

val_err = 'Input must be a number.'

def test_usr(msg):
    """Return bool on user input given message (Y,N)"""
    while True:
        usr = input(f'{msg} (y, n): ')

        if usr.lower() == 'y': return True

        if usr.lower() == 'n': return False


def get_year():
    """Returns desired year as an integer."""
    while True:
        year = input('\nYear: ')

        if year.isdigit(): return int(year)

        else: print(val_err)


def get_month():
    """Returns desired month as an integer."""
    while True:
        month = input('\nMonth: ')

        if month.isdigit():
            month = int(month)

            if month in range(1, 13): return month

            else: print('Month must be between 1 and 12.')

        else: print(val_err)


def get_day(year, month):
    """Returns desired day as an integer."""
    while True:
        day = input('\nDay: ')

        if day.isdigit():
            day = int(day)
            wk_day, days = monthrange(year, month)
            if day in range(1, days+1): return day

            else: print(f'Day must be between 1 and {days}.')

        else: print(val_err)


def get_hour():
    """Returns desired hour as an integer."""
    while True:
        hour = input('\nHour: ')

        if hour.isdigit():
            hour = int(hour)

            if hour in range(24): return hour

            else: print('Hour must be between 0 and 23.')

        else: print(val_err)


def get_minute():
    """Returns desired minute as an integer."""
    while True:
        minute = input('\nMinute: ')

        if minute.isdigit():
            minute = int(minute)

            if minute in range(60): return minute

            else: print('Minute must be between 0 and 59.')

        else: print(val_err)


def get_datetime_obj():
    """Returns a valid datetime object from the datetime library"""
    year = get_year()
    month = get_month()
    day = get_day(year, month)
    hour = get_hour()
    minute = get_minute()

    date = datetime(year, month, day, hour, minute)

    return date
