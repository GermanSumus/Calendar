import datetime

current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
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
        year = input('\nEnter in Year xxxx: ')

        if year.isdigit():
            year = int(year)

            if year >= current_year:
                return year
            else:
                print(f'Year must be greater than {current_year - 1}')
        else:
            print(val_err)

def get_month(year):
    """Returns desired month in the form of an integer."""
    while True:
        month = input('\nEnter in month: ')

        if month.isdigit():
            month = int(month)

            if year == current_year:
                if month in range(current_month, 13):
                    return month
                else:
                    print(f'Month must be between {current_month} and 12.')
            elif month in range(1, 13):
                return month
            else:
                print(f'Month must be between 1 and 12.')
        else:
            print(val_err)

def get_day(year, month):
    """Returns desired day in the form of an integer."""
    while True:
        day = input('\nEnter in day: ')

        if day.isdigit():
            day = int(day)

            if year == current_year and month == current_month:
                if day in range(current_day, 32):
                    return day
                else:
                    print(f'Day must be between {current_day} and 31.')
            elif day in range(1, 32):
                return day
            else:
                print(f'Day must be between 1 and 31.')
        else:
            print(val_err)


def sani_date():
    """Returns a valid datetime object from the datetime library"""
    year = get_year()
    month = get_month(year)
    day = get_day(year, month)

    date = datetime.datetime.strptime(f'{year} {month} {day}', '%Y %m %d')

    return date

def sani_time():
    """Returns a valid time string to be interpreted as a datetime object"""
    time = input('Enter in time "x:xx" : ')
    valid = False
    while not valid:
        t = time.replace(':', '', 1)
        t = t.replace(' ', '')
        if t.isdigit() and len(t) >= 3:
            if int(t[-2:]) < 60:
                if int(t[0]) == 0:
                    t = t.replace('0', '', 1)
                if len(t) == 4:
                    if int(t[:2]) < 13:
                        valid = True
                else:
                    valid = True
            else:
                time = input('Enter in time "x:xx" : ')
        else:
            time = input('Enter in time "x:xx" : ')
    test_usr('Is this in the morning?')
