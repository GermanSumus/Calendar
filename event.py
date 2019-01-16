from sanitize import sani_date

class Event(object):
    """An event with datetime features """
    def __init__(self):
        self.date = sani_date()
        self.time = sani_date()
