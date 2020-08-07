import unittest

from models.record import Record


class TestRecord(unittest.TestCase):
    def setUp(self):
        self.record = Record("13-04-2020", "Cat is sick.")

    def test_record_has_date(self):
        expected = "13-04-2020"
        actual = self.record.date
        self.assertEqual(expected, actual)

    def test_record_has_entry(self):
        expected = "Cat is sick."
        actual = self.record.entry
        self.assertEqual(expected, actual)

    def test_record_has_None_id(self):
        actual = self.record.id
        self.assertIsNone(actual)

    def test_record_can_get_id(self):
        self.record.id = 16
        expected = 16
        actual = self.record.id
        self.assertEqual(expected, actual)
