from datetime import datetime

current_year = datetime.now().year
current_month = datetime.now().month
current_day = datetime.now().day
val_err = 'Input must be a number.'

def test_usr(msg):
    """Return bool on user input given message (Y,N)"""
    usr = input(f'{msg} Yes or No? (Y, N) ')
    valid = False
    while not valid:
        if usr.lower() in ' yn':
            valid = True
            if usr.lower() == 'y':
                return True
        else:
            usr = input(f'{msg} Yes or No? (Y, N) ')

def get_year():
    """Returns desired year in the form of an integer."""
    while True:
        year = input('\nYear: ')

        if year.isdigit(): return int(year)

        else: print(val_err)

def get_month(year):
    """Returns desired month in the form of an integer."""
    while True:
        month = input('\nMonth: ')

        if month.isdigit():
            month = int(month)

            if month in range(1, 13): return month
            
            else: print(f'Month must be between 1 and 12.')
        
        else: print(val_err)

def get_day(year, month):
    """Returns desired day in the form of an integer."""
    while True:
        day = input('\nDay: ')

        if day.isdigit():
            day = int(day)

            if day in range(1, 32): return day
            
            else: print(f'Day must be between 1 and 31.')
        
        else: print(val_err)


def sani_date():
    """Returns a valid datetime object from the datetime library"""
    year = get_year()
    month = get_month(year)
    day = get_day(year, month)

    date = datetime.strptime(f'{month} {day} {year}', '%m %d %Y').date()

    return date

def get_hour():
    """Returns desired hour in the form of an integer."""
    while True:
        hour = input('\nHour: ')
        
        if hour.isdigit():
            hour = int(hour)

            if hour in range(24): return hour
            
            else: print(f'Hour must be between 0 and 23.')
        
        else: print(val_err)

def get_minute():
    """Returns desired minute in the form of an integer."""
    while True:
        minute = input('\nMinute: ')
        
        if minute.isdigit():
            minute = int(minute)

            if minute in range(60): return minute
            
            else: print(f'Minute must be between 0 and 59.')
        
        else: print(val_err)

def sani_time():
    """Returns a valid time string to be interpreted as a datetime object"""
    hour = get_hour()
    minute = get_minute()
    time = f'{hour}:{minute}'

    return time
