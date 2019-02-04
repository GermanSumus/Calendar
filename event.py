from datetime import datetime, timedelta


class Event():
    """An event with datetime features """

    def __init__(self, date, description):
        self.datetime = date
        self.update(self.datetime)
        self.description = description

    def update(self, date):
        self.day = date.strftime('%A')
        self.date = date.strftime('%B %d, %Y')
        self.time = date.strftime('%H:%M')
        self.year = date.strftime('%Y')
        # The following strftime is platform dependent
        self.month = date.strftime('%-m')

    def __str__(self):
        return f'\n{self.description.title()} scheduled for {self.day}, {self.date} at {self.time}.'

    def move(self, week=0, day=0, hour=0, minute=0):
        self.datetime += timedelta(weeks=week, days=day, hours=hour, minutes=minute)
        self.update(self.datetime)

    def get_date(self):
        return self.date
