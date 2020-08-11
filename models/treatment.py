import datetime
from models.date_helper import DateHelper


class Treatment:
    def __init__(self, description, duration, recovery, cost, animal, id=None):
        self.description = description
        self.duration = duration
        self.recovery = recovery
        self.cost = cost
        self.animal = animal
        self.id = id
        self.end_date = None
