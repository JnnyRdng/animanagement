import unittest

from models.address import Address


class TestAddress(unittest.TestCase):
    def setUp(self):
        self.address = Address(71, "Princes Street", "Edinburgh", "eh1 1aa")

    def test_address_number(self):
        expected = 71
        actual = self.address.number
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

    def test_address_printable_number_and_street(self):
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
