import unittest

from models.vet import Vet


class TestVet(unittest.TestCase):
    def setUp(self):
        self.vet = Vet("Kevin", "Bacon")

    def test_vet_has_first_name(self):
        expected = "Kevin"
        actual = self.vet.first_name
        self.assertEqual(expected, actual)

    def test_vet_has_last_name(self):
        expected = "Bacon"
        actual = self.vet.last_name
        self.assertEqual(expected, actual)

    def test_vet_has_None_as_id(self):
        actual = self.vet.id
        self.assertIsNone(actual)

    def test_vet_can_get_id(self):
        self.vet.id = 100
        expected = 100
        actual = self.vet.id
        self.assertEqual(expected, actual)
