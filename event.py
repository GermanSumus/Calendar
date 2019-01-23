from datetime import datetime

class Event():
    """An event with datetime features """
    def __init__(self, date, time):
        self.date = date
        self.time = time

    def print_event_details(self):
        formatted_date = self.date.strftime('%A, %B %d, %Y')
        
        print(f'\nEvent scheduled for {formatted_date} at {self.time}.')

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time