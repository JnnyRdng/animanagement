import unittest

from models.vet import Vet
from models.owner import Owner
from models.animal import Animal


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.vet = Vet("Mark", "Bridges")
        self.owner = Owner("Kevin", "Stevens", "015825536874", "kevin@mail.com")
        self.animal = Animal(
            "Fluff", "04-01-2018", "Dog", self.owner, self.vet, "06-08-2020"
        )

    def test_animal_has_name(self):
        expected = "Fluff"
        actual = self.animal.name
        self.assertEqual(expected, actual)

    def test_animal_has_dob(self):
        expected = "04-01-2018"
        actual = self.animal.dob
        self.assertEqual(expected, actual)

    def test_animal_species(self):
        expected = "Dog"
        actual = self.animal.species
        self.assertEqual(expected, actual)

    def test_animal_has_owner(self):
        expected = "kevin@mail.com"
        actual = self.animal.owner.email
        self.assertEqual(expected, actual)

    def test_animal_has_vet(self):
        expected = "Mark"
        actual = self.animal.vet.first_name
        self.assertEqual(expected, actual)

    def test_admitted_date(self):
        expected = "06-08-2020"
        actual = self.animal.date_admitted
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
