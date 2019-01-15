import datetime
from sanitize import test_usr
from event import Event

def make_year(year=datetime.datetime.now().year):
    """This returns a yearly calendar as shown above"""
    cal = {year: {}}
    thirty_one = [1,3,5,7,8,10,12]
    for month in range(1,13):
        if month in thirty_one:
            days = dict(zip([x for x in range(1,32)], [[] for x in range(1,32)]))
            cal[year][month] = days
        elif month == 2:
            days = dict(zip([x for x in range(1,29)], [[] for x in range(1,29)]))
            cal[year][month] = days
        else:
            days = dict(zip([x for x in range(1,31)], [[] for x in range(1,31)]))
            cal[year][month] = days

    with open('cal.dict', 'w') as file:
        file.write(cal.__repr__())
    return cal

def add_event():
    if test_usr('Need to add something?'):
        print("YOU GOT IT, ONE EVENT OBJECT COMING RIGHT AFTER THESE MESSAGES")
        e_obj = Event()
        print(e_obj.datetime)
