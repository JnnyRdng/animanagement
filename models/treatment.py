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

    def start_treatment(self, time=None):
        if time is None:
            dh = DateHelper()
            self.start = dh.now()
        else:
            self.start = time

    def total(self, duration):
        dh = DateHelper()
        times = dh.list_delta(duration)
        string = ""
        if times[0] > 0:
            string += f"{times[0]} days"
        if times[1] > 0:
            if string != "":
                string += ", "
            string += f"{times[1]} hrs"
        if string != "":
            string += ", "
        string += f"{times[2]} mins"
        return string

    def print_start(self):
        dh = DateHelper()
        start_time = dh.print_nice(self.start)
        return start_time

    def print_duration(self):
        dh = DateHelper()
        treatment_time = self.start + self.duration
        return dh.print_nice(treatment_time)

    def print_recovery(self):
        dh = DateHelper()
        recovery_time = self.start + self.duration + self.recovery
        return dh.print_nice(recovery_time)
