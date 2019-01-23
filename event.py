from datetime import timedelta
from sanitize import sani_date, sani_time

class Event(object):
    """An event with datetime features """
    def __init__(self):
        self.date = sani_date()
#        self.time = sani_time()

    def move(self, week=0, day=0, hour=0, minute=0):
        self.date = self.date + timedelta(weeks=week, days=day, hours=hour, minutes=minute)
