class Animal:
    def __init__(
        self, name, dob, species, owner, vet, date_admitted, checked_in=True, id=None
    ):
        self.name = name
        self.dob = dob
        self.species = species
        self.owner = owner
        self.vet = vet
        self.date_admitted = date_admitted
        self.checked_in = checked_in
        self.id = id
        self.records = 0

    def check_out(self):
        # if already checked out, return None
        # else check out and return True
        if self.checked_in:
            self.checked_in = False
            return True

    def check_in(self):
        # if already checked in, return None
        #  else check in and return True
        if not self.checked_in:
            self.checked_in = True
            return True

    def set_records(self, num):
        self.records = num
