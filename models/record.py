from models.date_helper import DateHelper


class Record:
    def __init__(self, date, entry, animal, id=None):
        self.date = date
        self.entry = entry
        self.animal = animal
        self.id = id

    def print_date(self, which):
        dh = DateHelper()
        return getattr(dh, which)(self.date)
