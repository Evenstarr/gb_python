class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def make_date(cls, string_date):
        try:
            day, month, year = map(int, string_date.split("-"))
            return cls(day, month, year)
        except (TypeError, ValueError):
            return "Invalid date format"

    @staticmethod
    def validate_date(string_date):
        try:
            day, month, year = map(int, string_date.split("-"))
            return day in range(1, 32) and month in range(0, 13) and year > 0
        except (TypeError, ValueError):
            return False


date = Date.make_date("04-40-2020")
print(date)
is_date_valid = Date.validate_date("04-10-2020")
print(is_date_valid)
