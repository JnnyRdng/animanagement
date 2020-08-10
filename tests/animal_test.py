import unittest, datetime

from models.vet import Vet
from models.address import Address
from models.owner import Owner
from models.animal import Animal


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.vet = Vet("Mark", "Bridges")
        self.address = Address("9", "Big Road", "Vatican City", "PO1 1PE")
        self.owner = Owner(
            "Kevin", "Stevens", self.address, "015825536874", "kevin@mail.com"
        )
        self.animal = Animal(
            "Fluff",
            datetime.datetime.strptime("04-01-2018", "%d-%m-%Y"),
            "Dog",
            "Greyhound",
            self.owner,
            self.vet,
            "06-08-2020",
        )
        self.now = datetime.datetime.strptime(
            "10-08-2020 12:20:52", "%d-%m-%Y %H:%M:%S"
        )

    def test_animal_has_name(self):
        expected = "Fluff"
        actual = self.animal.name
        self.assertEqual(expected, actual)

    # def test_animal_has_dob(self):
    #     expected = "04-01-2018"
    #     actual = self.animal.dob
    #     self.assertEqual(expected, actual)

    def test_animal_species(self):
        expected = "Dog"
        actual = self.animal.species
        self.assertEqual(expected, actual)

    def test_animal_breed(self):
        expected = "Greyhound"
        actual = self.animal.breed
        self.assertEqual(expected, actual)

    def test_animal_has_owner(self):
        expected = "kevin@mail.com"
        actual = self.animal.owner.email
        self.assertEqual(expected, actual)

    def test_animal_has_vet(self):
        expected = "Mark"
        actual = self.animal.vet.first_name
        self.assertEqual(expected, actual)

    def test_registered_date(self):
        expected = "06-08-2020"
        actual = self.animal.date_registered
        self.assertEqual(expected, actual)

    def test_checked_in_default(self):
        expected = True
        actual = self.animal.checked_in
        self.assertEqual(expected, actual)

    def test_checked_out(self):
        self.animal.check_out()
        expected = False
        actual = self.animal.checked_in
        self.assertEqual(expected, actual)

    def test_checked_out_returns_True(self):
        expected = True
        actual = self.animal.check_out()
        self.assertEqual(expected, actual)

    def test_animal_already_checked_out_returns_None(self):
        self.animal.check_out()
        actual = self.animal.check_out()
        self.assertIsNone(actual)

    def test_checked_in(self):
        self.animal.check_in()
        expected = True
        actual = self.animal.checked_in
        self.assertEqual(expected, actual)

    def test_checked_in_returns_True(self):
        actual = self.animal.check_in()
        self.assertIsNone(actual)

    def test_animal_already_checked_in_returns_None(self):
        self.animal.check_in()
        actual = self.animal.check_in()
        self.assertIsNone(actual)

    def test_animal_has_None_id(self):
        actual = self.animal.id
        self.assertIsNone(actual)

    def test_animal_can_get_id(self):
        self.animal.id = 7816
        expected = 7816
        actual = self.animal.id
        self.assertEqual(expected, actual)

    def test_animal_has_num_records(self):
        expected = 0
        actual = self.animal.records
        self.assertEqual(expected, actual)

    def test_set_num_records(self):
        self.animal.set_records(5)
        expected = 5
        actual = self.animal.records
        self.assertEqual(expected, actual)

    def test_set_num_records_different_number(self):
        self.animal.set_records(10)
        expected = 10
        actual = self.animal.records
        self.assertEqual(expected, actual)

    def test_printable_date(self):
        expected = "10 Aug 2020"
        actual = self.animal.printable_date(self.now)
        self.assertEqual(expected, actual)

    def test_printable_datetime(self):
        expected = "12:20:52 10 Aug 2020"
        actual = self.animal.printable_datetime(self.now)
        self.assertEqual(expected, actual)

    def test_printable_age(self):
        expected = "2 years old"
        actual = self.animal.get_age(self.now)
        self.assertEqual(expected, actual)
