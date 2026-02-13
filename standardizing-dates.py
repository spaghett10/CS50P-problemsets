"""
Implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. 
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""

import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():

    date = input("Date: ").strip() #Prompt user for date

    validate(date) #Ensure input date follows either AD or text format


def validate(user_date):
    anno_date = r"(?P<mm>\d{1,2})/(?P<dd>\d{1,2})/(?P<yyyy>\d{4})" #Regex pattern for AD format
    match_anno = re.fullmatch(anno_date, user_date)

    text_date = r"(?P<mon>\w+)\s(?P<day>\d{1,2}),\s(?P<year>\d{4})" #Regex pattern for text format
    match_text = re.fullmatch(text_date, user_date)

    if match_anno != None: #Pass anno date match through anno conversion function
        return anno_conversion(match_anno)

    elif match_text != None: #Pass text match through text conversion function
        return text_conversion(match_text)

    else:
        main()

def text_conversion(mondayyear): #Converts match object to yyyy-mm-dd
    didnotBreak = True
    for month in months: # Loop of list to convert text month to number and validate month input
        if month == mondayyear.group("mon"):
            mon = months.index(month) + 1
            didnotBreak = False
            break
    if didnotBreak:
        main() #If user input month does not match month in list, reprompt user for date

    if 1 <= int(mondayyear.group("day")) <= 31: #Confirming that the day is a valid input between 1 and 31
        day = int(mondayyear.group("day"))
    else:
        main() #If fail, reprompt user for date

    year = mondayyear.group("year")

    print(f"{year}-{mon:02}-{day:02}")

def anno_conversion(mmddyyyy): #Converts match object to yyyy-mm-dd
    if 1 <= int(mmddyyyy.group("mm")) <= 12: #Confirming that the month is a valid input between 1 and 12
        mm = int(mmddyyyy.group("mm"))
    else:
        main() #If fail, reprompt user for date

    if 1 <= int(mmddyyyy.group("dd")) <= 31: #Confirming that the day is a valid input between 1 and 31
        dd = int(mmddyyyy.group("dd"))
    else:
        main() #If fail, reprompt user for date

    yyyy = mmddyyyy.group("yyyy")

    print(f"{yyyy}-{mm:02}-{dd:02}")

main()
