"""
Implement a program that:
Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
"""

import random

def main():
    valid_level = get_level() #Validate level input

    x = generate_integer(valid_level) #Generate random numbers for first problem
    y = generate_integer(valid_level)

    score = 0

    ##Creation of 10-problem loop
    for _ in range(10):
        correct_answer = x + y
        tries = 3 #3 attempt limit

        #3-try loop to validate input answers
        while True:
            if tries == 0: #Print correct answer and break loop after 3 try limit
                print(f"{x} + {y} = {correct_answer}")
                break
            try:
                input_answer = input(f"{x} + {y} = ")
                if input_answer != str(correct_answer): #If answer is incorrect, exception raised
                    raise ValueError
            except ValueError:
                tries -= 1 #tries = tries - 1
                print("EEE")
            else:
                score += 1 #If no exception raised, score increases and loop broken
                break

        x = generate_integer(valid_level)
        y = generate_integer(valid_level) #Generation of new integers for next problem

    print(f"Score: {score}")

##Function to validate level input
def get_level():
    while True: #Infinite loop to obtain valid level input of either 1, 2, or 3 and generate random numbers for first problem
        choice_level = input("Level: ")
        try:
            if int(choice_level) not in [1,2,3]:
                raise ValueError
        except ValueError:
            pass
        else:
            return choice_level

##Function to generate random integers depending on level input
def generate_integer(level): 
    if level == "1":
        return random.randint(0,9)
    elif level == "2":
        return random.randint(10,99)
    elif level == "3":
        return random.randint(100,999)

if __name__ == "__main__":
    main()
