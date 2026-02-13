"""
Implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.

"before.csv" CSV file to be cleaned up:

name,house
"Abbott, Hannah",Hufflepuff
"Bell, Katie",Gryffindor
"Bones, Susan",Hufflepuff
"Boot, Terry",Ravenclaw
"Brown, Lavender",Gryffindor
"Bulstrode, Millicent",Slytherin
"Chang, Cho",Ravenclaw
"Clearwater, Penelope",Ravenclaw
"Crabbe, Vincent",Slytherin
"Creevey, Colin",Gryffindor
"Creevey, Dennis",Gryffindor
"Diggory, Cedric",Hufflepuff
"Edgecombe, Marietta",Ravenclaw
"Finch-Fletchley, Justin",Hufflepuff
"Finnigan, Seamus",Gryffindor
"Goldstein, Anthony",Ravenclaw
"Goyle, Gregory",Slytherin
"Granger, Hermione",Gryffindor
"Johnson, Angelina",Gryffindor
"Jordan, Lee",Gryffindor
"Longbottom, Neville",Gryffindor
"Lovegood, Luna",Ravenclaw
"Lupin, Remus",Gryffindor
"Malfoy, Draco",Slytherin
"Malfoy, Scorpius",Slytherin
"Macmillan, Ernie",Hufflepuff
"McGonagall, Minerva",Gryffindor
"Midgen, Eloise",Gryffindor
"McLaggen, Cormac",Gryffindor
"Montague, Graham",Slytherin
"Nott, Theodore",Slytherin
"Parkinson, Pansy",Slytherin
"Patil, Padma",Gryffindor
"Patil, Parvati",Gryffindor
"Potter, Harry",Gryffindor
"Riddle, Tom",Slytherin
"Robins, Demelza",Gryffindor
"Scamander, Newt",Hufflepuff
"Slughorn, Horace",Slytherin
"Smith, Zacharias",Hufflepuff
"Snape, Severus",Slytherin
"Spinnet, Alicia",Gryffindor
"Sprout, Pomona",Hufflepuff
"Thomas, Dean",Gryffindor
"Vane, Romilda",Gryffindor
"Warren, Myrtle",Ravenclaw
"Weasley, Fred",Gryffindor
"Weasley, George",Gryffindor
"Weasley, Ginny",Gryffindor
"Weasley, Percy",Gryffindor
"Weasley, Ron",Gryffindor
"Wood, Oliver",Gryffindor
"Zabini, Blaise",Slytherin
"""

import sys
import csv

def main():
    input, output = validate_input()
    rewrite(input, output)

def rewrite(input_file, output_file):

    students1 = [] #Creation of 1st list for dict with full name and house keys
    with open(input_file) as file1:
        reader = csv.DictReader(file1)
        for row in reader:
            students1.append({"full_name": row["name"], "house": row["house"]})

    students2 = [] #Creation of 2nd list for dict with first name, last name and house keys
    for row in students1:
        last, first = row["full_name"].split(", ") #Splitting of first key in 1st list into 2 separate variables
        students2.append({"first": first, "last": last, "house": row["house"]})

    with open(output_file, "w") as file2: #Writing of new file with 2nd list that has all three necessary keys
        writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
        writer.writeheader() #Include header
        for row in students2:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

def validate_input():
    #First validate length of command line arguments
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    #Next validate quality of command line arguments for correct and valid file types
    try:
        file_name, ext = sys.argv[1].split(".")
    except ValueError:
        sys.exit(f"Could not read {sys.argv[1]}.")
    else:
        if ext != "csv":
            sys.exit(f"Could not read {sys.argv[1]}.")

    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}.")
    else:
        return sys.argv[1], sys.argv[2]

if __name__ == "__main__":
    main()


""" 
Cleaned up CSV file:

first,last,house
Hannah,Abbott,Hufflepuff
Katie,Bell,Gryffindor
Susan,Bones,Hufflepuff
Terry,Boot,Ravenclaw
Lavender,Brown,Gryffindor
Millicent,Bulstrode,Slytherin
Cho,Chang,Ravenclaw
Penelope,Clearwater,Ravenclaw
Vincent,Crabbe,Slytherin
Colin,Creevey,Gryffindor
Dennis,Creevey,Gryffindor
Cedric,Diggory,Hufflepuff
Marietta,Edgecombe,Ravenclaw
Justin,Finch-Fletchley,Hufflepuff
Seamus,Finnigan,Gryffindor
Anthony,Goldstein,Ravenclaw
Gregory,Goyle,Slytherin
Hermione,Granger,Gryffindor
Angelina,Johnson,Gryffindor
Lee,Jordan,Gryffindor
Neville,Longbottom,Gryffindor
Luna,Lovegood,Ravenclaw
Remus,Lupin,Gryffindor
Draco,Malfoy,Slytherin
Scorpius,Malfoy,Slytherin
Ernie,Macmillan,Hufflepuff
Minerva,McGonagall,Gryffindor
Eloise,Midgen,Gryffindor
Cormac,McLaggen,Gryffindor
Graham,Montague,Slytherin
Theodore,Nott,Slytherin
Pansy,Parkinson,Slytherin
Padma,Patil,Gryffindor
Parvati,Patil,Gryffindor
Harry,Potter,Gryffindor
Tom,Riddle,Slytherin
Demelza,Robins,Gryffindor
Newt,Scamander,Hufflepuff
Horace,Slughorn,Slytherin
Zacharias,Smith,Hufflepuff
Severus,Snape,Slytherin
Alicia,Spinnet,Gryffindor
Pomona,Sprout,Hufflepuff
Dean,Thomas,Gryffindor
Romilda,Vane,Gryffindor
Myrtle,Warren,Ravenclaw
Fred,Weasley,Gryffindor
George,Weasley,Gryffindor
Ginny,Weasley,Gryffindor
Percy,Weasley,Gryffindor
Ron,Weasley,Gryffindor
Oliver,Wood,Gryffindor
Blaise,Zabini,Slytherin
"""
