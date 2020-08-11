import unittest

from models.vet import Vet


class TestVet(unittest.TestCase):
    def setUp(self):
        self.vet = Vet("Kevin", "Bacon", 5)

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

    def test_max_animals_is_5(self):
        expected = 5
        actual = self.vet.max_animals
        self.assertEqual(expected, actual)

    def test_animal_count_is_0(self):
        expected = 0
        actual = self.vet.animal_count
        self.assertEqual(expected, actual)

    def test_set_count(self):
        self.vet.set_count(6)
        expected = 6
        actual = self.vet.animal_count
        self.assertEqual(expected, actual)

    def test_vet_busy(self):
        expected = False
        actual = self.vet.busy
        self.assertEqual(expected, actual)

    def test_set_vet_busy(self):
        self.vet.set_busy()
        expected = True
        actual = self.vet.busy
        self.assertEqual(expected, actual)

    def test_set_vet_available(self):
        self.vet.set_busy()
        self.vet.set_available()
        expected = False
        actual = self.vet.busy
        self.assertEqual(expected, actual)
