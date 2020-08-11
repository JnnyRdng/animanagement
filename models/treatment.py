import datetime
from models.date_helper import DateHelper


class Treatment:
    def __init__(self, description, duration, recovery, cost, animal, id=None):
        self.description = description
        self.start = None
        self.duration = duration
        self.recovery = recovery
        self.cost = cost
        self.animal = animal
        self.id = id

    def start_treatment(self):
        dh = DateHelper()
        self.start = dh.now()
