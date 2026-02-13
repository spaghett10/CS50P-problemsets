"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

 1. All vanity plates must start with at least two letters
 2. Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
 3. Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’
 4. No periods, spaces, or punctuation marks are allowed

 Instructions: Implement a program that prompts the user for a vanity plate and then output "Valid" if meets all of the requirements or "Invalid" if it does not. 
 Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#Defining function to ensure first two characters are alphabetic
def letters_start(aa):
    if len(aa) >= 2 and aa[0:1].isalpha() == True:
        return True

#Defining function to check plate character length and that there are no special characters
def min_max(abcdef):
    if 2 <= len(abcdef) <= 6 and abcdef.isalnum() == True:
        return True

#Defining function to check that numbers are not in middle and are at end of plate
def numeric(xyz):
    
    #Creating nested loop to check sequentially whether each character is a number
    for character in xyz: #Outer loop to check through each character
        numbers = "0123456789"
        
    				for number in numbers: #Inner loop to check whether character is a number 0-9
            if character == number and number == "0":
                return False #Breaking function if first encountered numeric character is a 0
            elif character == number:
                _, number_string = xyz.split(number, 1) #Splitting xyz by first encountered number as separator
                if number_string.isdigit() is True:
                    return True #Breaking function/Returning true if number_string is all numbers
                else:
                    return False #Breaking function if an alphabetical character is encountered in number_string

    return True #Returning true if xyz is all alphabetical, no numbers

def is_valid(s):
    if letters_start(s) == True and min_max(s) == True and numeric(s) == True:
        return True

main()
