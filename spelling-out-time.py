"""
Implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then prints how old they are in minutes, rounded to the nearest integer,using English words instead of numerals, just like the song from Rent, without any and between words. 
Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. 
And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. 
"""

from datetime import date
import inflect
from re import search
import sys

p = inflect.engine()

class Calculator:
    def __init__(self, InputDate):
        self.InputDate = InputDate

    def __sub__(self, OtherDate):
        difference = self.InputDate - OtherDate.InputDate
        return Calculator(difference)

    def __str__(self):
        # isolate numbers of days from timedelta object via regex
        DaysDifference = search(r"^(?P<days>\d+) days", str(self.InputDate))

        # convert days to minutes
        MinutesDifference = int(DaysDifference.group("days")) * 24 * 60

        # convert numbers to text via inflect
        formatted_output = p.number_to_words(MinutesDifference, andword = "").capitalize()
        return f"{formatted_output} minutes"

def main():
    # obtain user birthday
    birthday = input("Date of Birth: ")

    # instantiate 2 Calculator objects for birthday and current date
    start_date = Calculator(validate(birthday))
    end_date = Calculator(validate(str(date.today())))

    diff = end_date - start_date
    print(diff)

def validate(input_date):
    # 1st check for correct date yyyy-mm-dd layout via regex
    if matches := search(r"^(?P<year>\d{4})-(?P<mon>\d{2})-(?P<day>\d{2})$", input_date):

        # 2nd check for valid year, month, and day inputs via date() method
        try:
            date(int(matches.group("year")), int(matches.group("mon")), int(matches.group("day")))
        except ValueError:
            sys.exit("Invalid date")

        # return date object of validated date if input date is not in future
        else:
            if int(matches.group("year")) > int(date.today().year):
                sys.exit("Invalid date")
            else:
                return date(int(matches.group("year")), int(matches.group("mon")), int(matches.group("day")))

    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
