"""
weekly_schedule():
Return the weeks schedule in a human readable by reading our calendar.
A week is seven days from today.
Our calendars are going to be in a txt file that will evaluate to:
    a dict containing        years as keys and calendar as a value.
    calendar is a dict of    months as keys and its days as a value.
    days is a list of        Event_objects or an empty list.
example: {2019: {1: {1:[], 2:[], ..} }, {2: {1:[], 2:[], ..}, ..},
          2020: {1: {1:[], 2:[], ..} }, {2: {1:[], 2:[], ..}, ..}}
"""
import datetime
from evaluate_calendar import read_cal
from manipulate_cal import make_year

def weekly_schedule(cal_file_path='cal.dict', now=datetime.datetime.now()):
    """Print out the weeks schedule for humans to read"""
    cal = read_cal()

    if len(cal) < 1: cal = make_year()

    #print(f'\n{now} \n***DAYS***\n{now + datetime.timedelta(days=6)}\n')
    print("\nPREVIEW OF THE WEEK")
    # BUG IN THE NEXT LINES BELOW. DATE CANT GO PAST 1/31/2019.
    for x in range(7):
        date = now + datetime.timedelta(days=x)
        day_events = cal[date.year][date.month][date.day]

        print('\t', date.strftime('%B %d, %Y'), day_events)
