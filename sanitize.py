import datetime

def test_usr(msg):
    """Return bool on user input given message (Y,N)"""
    usr = input(f'{msg} Yes or No? (Y, N) ')
    valid = False
    while not valid:
        if usr.lower() in 'yn':
            valid = True
            if usr.lower() == 'y':
                return True
        else:
            usr = input(f'{msg} Yes or No? (Y, N) ')

def sani_date():
    """Returns a valid datetime object from the datetime library"""
    year = input('Enter in Year xxxx: ')
    valid = False
    while not valid:
        if year.isdigit():
            if int(year) < datetime.datetime.now().year:
                print('Date error, try again.')
                year = input('Enter in Year xxxx: ')
            else:
                valid = True
        else:
            print('Value error, try again')
            year = input('Enter in Year xxxx: ')
    valid = False

    month = input('Enter in month: ')
    while not valid:
        if month.isdigit():
            if int(month) < datetime.datetime.now().month and int(month) < 13:
                print('Date error, try again.')
                month = input('Enter in month: ')
            else:
                valid = True
        else:
            print('Value error, try again')
            month = input('Enter in month: ')
    valid = False

    day = input('Enter in day: ')
    while not valid:
        if day.isdigit():
            if int(day) < datetime.datetime.now().day:
                print('Date error, try again.')
                day = input('Enter in day: ')
            else:
                valid = True
        else:
            print('Value error, try again')
            year = input('Enter in day: ')
    date = datetime.datetime.strptime(f'{year} {month} {day}', '%Y %m %d')

    return date
    
def sani_time():
    """Returns a valid time string to be interpreted as a datetime object"""
    time = input('Enter in time')
