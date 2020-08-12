import unittest

from models.address import Address
from models.owner import Owner


class TestOwner(unittest.TestCase):
    def setUp(self):
        self.address = Address("14", "Main Street", "Liverpool", "LI7 3RP")
        self.owner = Owner(
            "John", "Smith", self.address, "07752231146", "john.smith@mail.com"
        )

    def test_owner_has_first_name(self):
        expected = "John"
        actual = self.owner.first_name
        self.assertEqual(expected, actual)

    def test_owner_has_last_name(self):
        expected = "Smith"
        actual = self.owner.last_name
        self.assertEqual(expected, actual)

    def test_owner_has_tel(self):
        expected = "07752231146"
        actual = self.owner.tel
        self.assertEqual(expected, actual)

    def test_owner_has_email(self):
        expected = "john.smith@mail.com"
        actual = self.owner.email
        self.assertEqual(expected, actual)

    def test_owner_has_None_id(self):
        actual = self.owner.id
        self.assertIsNone(actual)

    def test_owner_can_get_id(self):
        self.owner.id = 90
        expected = 90
        actual = self.owner.id
        self.assertEqual(expected, actual)

    def test_owner_has_bill(self):
        expected = 0
        actual = self.owner.bill
        self.assertEqual(expected, actual)

    def test_owner_increase_bill(self):
        self.owner.increase_bill(50)
        expected = 50
        actual = self.owner.bill
        self.assertEqual(expected, actual)

    def test_owner_decrease_bill(self):
        self.owner.increase_bill(100)
        self.owner.decrease_bill(23)
        expected = 77
        actual = self.owner.bill
        self.assertEqual(expected, actual)

    def test_owner_address(self):
        expected = "Liverpool"
        actual = self.owner.address.city
        self.assertEqual(expected, actual)
