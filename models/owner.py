class Owner:
    def __init__(self, first_name, last_name, tel, email, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.email = email
        self.id = id
        self.animals = 0

    def set_animals(self, num):
        self.animals = num
