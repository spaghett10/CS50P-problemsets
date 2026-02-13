"""
Implement a function called convert that expects a string in any of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. 
9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM

Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). 
But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
"""

import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.search(r"(?P<hr1>\d{1,2}):?(?P<min1>\d{2})? (?P<era1>AM|PM) to (?P<hr2>\d{1,2}):?(?P<min2>\d{2})? (?P<era2>AM|PM)", s):

        #Validation of 1st time stamp: validating hour and minute numbers and adding 12 to hour if in PM
        if matches.group("era1") == "PM":
            if 0 < int(matches.group("hr1")) < 12: #Adding 12 to hour if in PM
                hr1_24 = int(matches.group("hr1")) + 12
            elif int(matches.group("hr1")) == 12: #Keeping 12PM as 12
                hr1_24 = 12
            else:
                raise ValueError
        elif matches.group("era1") == "AM":
            if 0 < int(matches.group("hr1")) < 12: #If AM, keeping hours as user entered if within 1-11
                hr1_24 = int(matches.group("hr1"))
            elif int(matches.group("hr1")) == 12: #Changing 12AM to 00
                hr1_24 = 00
            else:
                raise ValueError
        if matches.group("min1") == None: #Storing minutes as 00 if no minutes given in input (eg. 10 AM)
            min1_24 = "00"
        elif int(matches.group("min1")) < 60: #Keeping minutes as user entered if within 0-60
            min1_24 = matches.group("min1")
        else:
            raise ValueError

        #Validation of 2nd time stamp: validating hour and minute numbers and adding 12 to hour if in PM
        if matches.group("era2") == "PM":
            if 0 < int(matches.group("hr2")) < 12:
                hr2_24 = int(matches.group("hr2")) + 12
            elif int(matches.group("hr2")) == 12:
                hr2_24 = 12
            else:
                raise ValueError
        elif matches.group("era2") == "AM":
            if 0 < int(matches.group("hr2")) < 12:
                hr2_24 = int(matches.group("hr2"))
            elif int(matches.group("hr2")) == 12:
                hr2_24 = 00
            else:
                raise ValueError
        if matches.group("min2") == None:
            min2_24 = "00"
        elif int(matches.group("min2")) < 60:
            min2_24 = matches.group("min2")
        else:
            raise ValueError
    else:
        raise ValueError

    return f"{hr1_24:02}:{min1_24:02} to {hr2_24:02}:{min2_24:02}"

if __name__ == "__main__":
    main()
