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

    def print_nice(self, date):
        time = date.strftime("%-I:%M%p").lower()
        date = date.strftime("%-d %b %Y")
        return f"{time}, {date}"

    def print_format(self, date):
        return date.strftime("%Y-%m-%d")

    def print_datetime_local(self, date):
        return date.strftime("%Y-%m-%dT%H:%M")
