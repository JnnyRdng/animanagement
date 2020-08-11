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

    def time_delta(self, dmhs):
        time = dmhs.split(":")
        ints = [int(unit) for unit in time]
        return datetime.timedelta(
            days=ints[0], hours=ints[1], minutes=ints[2], seconds=ints[3]
        )

    def list_delta(self, delta):
        days = delta.days
        hours = delta.seconds // 3600
        minutes = delta.seconds // 60 % 60
        seconds = 0
        return [days, hours, minutes, seconds]

    def now(self):
        return datetime.datetime.now()
