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
    """Returns desired year as a string."""
    while True:
        year = input('\nYear: ')

        if year.isdigit(): 
            # f'{int(unit)}' gets rid of any zeros before number
            if int(year) < 10: return f'000{int(year)}'

            elif int(year) < 100: return f'00{int(year)}'
            
            elif int(year) < 1000: return f'0{int(year)}'
            
            else: return f'{int(year)}'
        
        else: print(val_err)

def get_month():
    """Returns desired month as a string."""
    while True:
        month = input('\nMonth: ')

        if month.isdigit():
            if int(month) in range(1, 13): return f'{int(month)}'
            
            else: print(f'Month must be between 1 and 12.')
        
        else: print(val_err)

def get_day():
    """Returns desired day as a string."""
    while True:
        day = input('\nDay: ')

        if day.isdigit():
            if int(day) in range(1, 32): return f'{int(day)}'
            
            else: print(f'Day must be between 1 and 31.')
        
        else: print(val_err)


def sani_date():
    """Returns a valid datetime object from the datetime library"""
    year = get_year()
    month = get_month()
    day = get_day()

    date = datetime.strptime(f'{month}{day}{year}', '%m%d%Y').date()

    return date

def get_hour():
    """Returns desired hour as a string."""
    while True:
        hour = input('\nHour: ')
        
        if hour.isdigit():
            if int(hour) in range(1, 13):
                if int(hour) < 10: return f'0{int(hour)}'
                
                else: return f'{int(hour)}'
            
            else: print(f'Hour must be between 1 and 12.')
        
        else: print(val_err)

def get_minute():
    """Returns desired minute as a string."""
    while True:
        minute = input('\nMinute: ')
        
        if minute.isdigit():
            if int(minute) in range(60):
                if int(minute) < 10: return f'0{int(minute)}'
                
                else: return f'{int(minute)}'
            
            else: print(f'Minute must be between 0 and 59.')
        
        else: print(val_err)

def get_am_pm():
    while True:
        am_pm = input('\nAM or PM: ')

        if am_pm.lower() == 'am': return 'AM'

        elif am_pm.lower() == 'pm': return 'PM'

        else: print("Enter 'am' or 'pm'.")

def sani_time():
    """Returns a valid time string to be interpreted as a datetime object"""
    hour = get_hour()
    minute = get_minute()
    am_pm = get_am_pm()
    time = f'{hour}:{minute} {am_pm}'

    return time
