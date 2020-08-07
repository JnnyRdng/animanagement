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

    def check_out(self):
        # if already checked out, return false
        # else check out and return true
        if self.checked_in:
            self.checked_in = False
            return True
        else:
            return False
