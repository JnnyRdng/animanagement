import unittest, datetime

from models.vet import Vet
from models.address import Address
from models.owner import Owner
from models.animal import Animal
from models.record import Record
from models.date_helper import DateHelper


class TestRecord(unittest.TestCase):
    def setUp(self):
        self.dh = DateHelper()
        self.vet = Vet("Mark", "Bridges")
        self.address = Address("14", "Park Street", "London", "W1A 2SC")
        self.owner = Owner(
            "Kevin", "Stevens", self.address, "015825536874", "kevin@mail.com"
        )
        self.animal = Animal(
            "Fluff",
            self.dh.make_date("2018-01-04"),
            "Dog",
            "Greyhound",
            self.owner,
            self.vet,
            self.dh.make_datetime("2020-08-06 13:05:00"),
        )
        self.animal.id = 763
        self.record = Record(
            self.dh.make_datetime("2020-05-03 17:09:03"), "Cat is sick.", self.animal
        )

    def test_record_has_date(self):
        expected = "5:09pm, 3 May 2020"
        actual = self.dh.print_nice(self.record.date)
        self.assertEqual(expected, actual)

    def test_record_has_entry(self):
        expected = "Cat is sick."
        actual = self.record.entry
        self.assertEqual(expected, actual)

    def test_record_has_animal_name(self):
        expected = "Fluff"
        actual = self.record.animal.name
        self.assertEqual(expected, actual)

    def test_record_has_animal_id(self):
        expected = 763
        actual = self.record.animal.id
        self.assertEqual(expected, actual)

    def test_record_has_None_id(self):
        actual = self.record.id
        self.assertIsNone(actual)

    def test_record_can_get_id(self):
        self.record.id = 16
        expected = 16
        actual = self.record.id
        self.assertEqual(expected, actual)

    def test_printed_date(self):
        expected = "5:09pm, 3 May 2020"
        actual = self.record.print_date("print_nice")
        self.assertEqual(expected, actual)
