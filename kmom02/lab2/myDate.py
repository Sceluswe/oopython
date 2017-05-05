"""
Date module for a date class, handling one date type.
"""

class Date:
    """
    A class keeping track of a date.
    """

    def __init__(self, int_year, int_month, int_day):
        """
        Constructor.
        """
        self.int_year = int_year
        self.int_month = int_month
        self.int_day = int_day

    def info(self):
        """
        Returns a date as a string, format yy-mm-dd
        """
        str_result = ""

        if self.int_year < 10:
            str_result += "0"
        str_result += str(self.int_year) + "-"

        if self.int_month < 10:
            str_result += "0"
        str_result += str(self.int_month) + "-"

        if self.int_day < 10:
            str_result += "0"
        str_result += str(self.int_day)

        return str_result

    def __lt__(self, other):
        """
        Smaller than operator.
        """
        return self.int_year < other.int_year and self.int_month < other.int_month and self.int_day < other.int_day
