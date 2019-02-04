import datetime
from json import dump

from sanitize import test_usr, get_datetime_obj, description
from event import Event
from evaluate_calendar import write_to_cal, read_cal


def make_year(year=datetime.datetime.now().year):
    """This returns a yearly calendar as shown above"""
    cal = {year: {}}
    thirty_one = [1,3,5,7,8,10,12]
    for month in range(1,13):
        if month in thirty_one:
            days = dict(zip([x for x in range(1,32)], [{} for x in range(1,32)]))
            cal[year][month] = days
        elif month == 2:
            days = dict(zip([x for x in range(1,29)], [{} for x in range(1,29)]))
            cal[year][month] = days
        else:
            days = dict(zip([x for x in range(1,31)], [{} for x in range(1,31)]))
            cal[year][month] = days

    with open('cal.dict', 'w') as file:
        dump(cal, file, indent=2)
    return read_cal()

def add_event():
    if test_usr('\nNeed to add something?'):
        print("\nCREATE EVENT")
        e_obj = Event(get_datetime_obj(), description())
        write_to_cal(e_obj)
        print(f'{e_obj} Added to calendar')
