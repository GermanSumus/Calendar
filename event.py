from sanitize import sani_datetime

class Event(object):
    """An event with datetime features """
    def __init__(self):
        self.datetime = sani_datetime()
