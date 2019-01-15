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

def sani_datetime():
    """Returns a valid datetime object from the datetime library"""
    return [1,2,3]
