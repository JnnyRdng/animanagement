class Vet:
    def __init__(self, first_name, last_name, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.max_animals = 5
        self.animal_count = 0

    def set_count(self, num):
        self.animal_count = num
