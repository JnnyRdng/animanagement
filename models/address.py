class Address:
    def __init__(self, number, street, city, postcode, id=None):
        self.number = number
        self.street = street
        self.city = city
        self.postcode = postcode
        self.id = id

    def printable(self):
        first_line = f"{str(self.number).upper()} {self.street.upper()}"
        second_line = f"{self.city.upper()}"
        postcode = "".join(self.postcode.split())
        third_line = f"{postcode.upper()}"
        return [first_line, second_line, third_line]
