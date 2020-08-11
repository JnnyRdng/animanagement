class Vet:
    def __init__(self, first_name, last_name, max_animals, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.max_animals = max_animals
        self.animal_count = 0
        self.busy = False

    def set_count(self, num):
        self.animal_count = num

    def set_busy(self):
        self.busy = True

    def set_available(self):
        self.busy = False
