"""
File: Ball8.py
-----------------------
This programme selects an answer at random to give to any yes/no question.
"""
# function for random operations
import random

# constant because the ball has 8 sides
EIGHT_BALL = 8

# pre-condition: person asks a question which needs a yes or no answer
# post-condition: a randomly selected number between 1 and 8 will generate a response, ready to be asked again

def eight_ball():
    answer = random.randint(1, EIGHT_BALL)
    if answer == 1:
        print("That is a difficult question, but I think so, yes.")
    if answer == 2:
            print("Ask again later.")
    if answer == 3:
        print("I will tell you later.")
    if answer == 4:
            print("It is not possible to tell you at the moment.")
    if answer == 5:
            print("Please rephrase the question.")
    if answer == 6:
            print("Definitely, no.")
    if answer == 7:
            print("Luckily for you, yes.")
    if answer == 8:
            print("Absolutely, yes.")

def main():
    line = input("Enter any question with a yes or no answer: ")
    print("Your question was: " + str(line) + ".")
    answer = eight_ball()

    while line != "":
        print()
        print("Thank you, why not run this game again and ask another question?")
        break

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
