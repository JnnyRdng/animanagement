import unittest

from models.address import Address
from models.owner import Owner


class TestAddress(unittest.TestCase):
    def setUp(self):
        self.address = Address(71, "Princes Street", "Edinburgh", "eh1 1aa")

    def test_address_num(self):
        expected = 71
        actual = self.address.num
        self.assertEqual(expected, actual)

    def test_address_street(self):
        expected = "Princes Street"
        actual = self.address.street
        self.assertEqual(expected, actual)

    def test_address_city(self):
        expected = "Edinburgh"
        actual = self.address.city
        self.assertEqual(expected, actual)

    def test_address_postcode(self):
        expected = "eh1 1aa"
        actual = self.address.postcode
        self.assertEqual(expected, actual)

    def test_address_has_None_id(self):
        actual = self.address.id
        self.assertIsNone(actual)

    def test_address_can_get_id(self):
        self.address.id = 12
        expected = 12
        actual = self.address.id
        self.assertEqual(expected, actual)

    def test_address_printable_num_and_street(self):
        expected = "71 PRINCES STREET"
        actual = self.address.printable()[0]
        self.assertEqual(expected, actual)

    def test_address_printable_city(self):
        expected = "EDINBURGH"
        actual = self.address.printable()[1]
        self.assertEqual(expected, actual)

    def test_address_printable_postcode(self):
        expected = "EH11AA"
        actual = self.address.printable()[2]
        self.assertEqual(expected, actual)

    def test_address_printable_full(self):
        expected = "71 PRINCES STREET EDINBURGH EH11AA"
        actual = " ".join(self.address.printable())
        self.assertEqual(expected, actual)
