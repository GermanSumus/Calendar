"""
weekly_schedule():
Return the weeks schedule in a human readable by reading our calendar.
A week is seven days from today.
"""
import datetime

from evaluate_calendar import read_cal
from manipulate_cal import make_year

def weekly_schedule(cal_file_path='cal.dict', now=datetime.datetime.now()):
    """Print out the weeks schedule for humans to read"""
    cal = read_cal()
    if len(cal) < 1: cal = make_year()
    print("\nPREVIEW OF THE WEEK")
    for x in range(7):
        date = now + datetime.timedelta(days=x)
        day_events = cal[str(date.year)][str(date.month)][str(date.day)]
        print('\t', date.strftime('%B %d, %Y'), day_events)
