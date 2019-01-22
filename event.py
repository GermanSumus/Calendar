class Event():
    """An event with datetime features """
    def __init__(self, date, time):
        self.date = date
        self.time = time

    def print_event_details(self):
        print(f'\nEvent scheduled for {self.date} at {self.time}.')

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time