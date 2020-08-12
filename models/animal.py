import datetime
from dateutil import relativedelta

from models.date_helper import DateHelper


class Animal:
    def __init__(
        self, name, dob, species, breed, owner, vet, date_registered, id=None,
    ):
        self.name = name
        self.dob = dob
        self.species = species
        self.breed = breed
        self.owner = owner
        self.vet = vet
        self.date_registered = date_registered
        self.checked_in = False
        self.id = id
        self.records = 0
        self.location = ""

    def set_records(self, num):
        self.records = num

    def get_age(self, until=datetime.datetime.now()):
        age = relativedelta.relativedelta(until, self.dob)
        periods = ["years", "months", "days"]
        age_string = "0 days old"
        for period in periods:
            time = getattr(age, period)
            if time == 0:
                continue
            elif time == 1:
                age_string = f"{time} {period[:-1]} old"
            else:
                age_string = f"{time} {period} old"
            break
        return age_string

    def print_dob(self, which):
        dh = DateHelper()
        return getattr(dh, which)(self.dob)

    def print_registered(self, which):
        dh = DateHelper()
        return getattr(dh, which)(self.date_registered)

    def where(self, treatment):
        dh = DateHelper()
        now = dh.now()
        if treatment is None:
            self.checked_in = False
            self.location = ""
            return
        elif now < treatment.start + treatment.duration:
            self.checked_in = True
            self.location = "treatment"
            return
        elif now < treatment.start + treatment.duration + treatment.recovery:
            self.checked_in = True
            self.location = "recovery"
            return
        else:
            self.checked_in = False
            self.location = ""
            return
