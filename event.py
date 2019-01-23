from datetime import datetime

class Event():
    """An event with datetime features """
    def __init__(self, date):
        self.date = date
        self.day = date.strftime('%A')
        self.date = date.strftime('%B %d, %Y')
        self.time = date.strftime('%H:%M')

    def __str__(self):
        return f'\nEvent scheduled for {self.day}, {self.date} at {self.time}.'

    def get_date(self):
        return self.date
