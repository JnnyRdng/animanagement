import unittest, datetime
from models.date_helper import DateHelper


class TestDateHelper(unittest.TestCase):
    def setUp(self):
        self.dh = DateHelper()
        self.date_str = "1999-08-01"
        self.datetime_str = "1998-05-02 14:08:00"
        self.date_obj = self.dh.make_date(self.date_str)
        self.datetime_obj = self.dh.make_datetime(self.datetime_str)

    def test_print_date(self):
        expected = "01 Aug 1999"
        actual = self.dh.print_date(self.date_obj)
        self.assertEqual(expected, actual)

    def test_print_datetime(self):
        expected = "14:08:00 02 May 1998"
        actual = self.dh.print_datetime(self.datetime_obj)
        self.assertEqual(expected, actual)

    def test_print_nice(self):
        expected = "2:08pm, 2 May 1998"
        actual = self.dh.print_nice(self.datetime_obj)
        self.assertEqual(expected, actual)
