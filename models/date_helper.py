import datetime


class DateHelper:
    def make_date(self, datestring):
        return datetime.datetime.strptime(datestring, "%Y-%m-%d")

    def make_datetime(self, datestring):
        return datetime.datetime.strptime(datestring, "%Y-%m-%d %H:%M:%S")

    def print_date(self, date):
        return date.strftime("%d %b %Y")

    def print_datetime(self, date):
        return date.strftime("%H:%M:%S %d %b %Y")
