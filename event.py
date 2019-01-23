from datetime import datetime

class Event():
    """An event with datetime features """
    def __init__(self, date):
        self.date = date

    def print_event_details(self):
        day = self.date.strftime('%A')
        date = self.date.strftime('%B %d, %Y')
        time = self.date.strftime('%H:%M')
        
        print(f'\nEvent scheduled for {day}, {date} at {time}.')

    def get_date(self):
        return self.date