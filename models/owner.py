class Owner:
    def __init__(self, first_name, last_name, address, tel, email, bill=0, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.tel = tel
        self.email = email
        self.id = id
        self.animals = 0
        self.bill = bill

    def increase_bill(self, amount):
        self.bill += amount

    def decrease_bill(self, amount):
        self.bill -= amount
