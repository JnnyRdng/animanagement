import unittest

from models.owner import Owner


class TestOwner(unittest.TestCase):
    def setUp(self):
        self.owner = Owner("John", "Smith", "07752231146", "john.smith@mail.com")

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

    def test_owner_has_num_animals(self):
        expected = 0
        actual = self.owner.animals
        self.assertEqual(expected, actual)

    def test_set_num_animals(self):
        self.owner.set_animals(4)
        expected = 4
        actual = self.owner.animals
        self.assertEqual(expected, actual)

    def test_set_num_animals_different_number(self):
        self.owner.set_animals(8)
        expected = 8
        actual = self.owner.animals
        self.assertEqual(expected, actual)
