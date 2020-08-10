
"""
File: rock_paper_scissors.py
-----------------------
This programme creates a game of rock, paper, scissors which a person can play against this computer programme.
The best of 3 goes is the winner.
# pre-condition: person asked to choose rock, paper, scissors
# post-condition: the computer gives her choice, she evaluates who has won and counts the scores, best of 3 wins

Rules:-

1. Scissors cut paper
2. Paper covers rock
3. Rock crushes scissors

"""
import random

results = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]
moves = [result[1] for result in results]

player_score, computer_score = (0, 0)

player = input("Enter rock/paper/scissors/(quit to finish game): ").lower()

while player != "quit":
    computer = random.choice(moves)
    print("You chose {}, I chose {}".format(player, computer))
    if player == computer:
        print("It's a tie!")
    elif (player, computer) in results:
        print("You win!")
        player_score += 1
    elif (computer, player) in results:
        print ("I win!")
        computer_score += 1
    else:
        print("Invalid input. Try again.")
    player = input("Enter rock/paper/scissors/(quit to finish game): ").lower()

    if player_score == 3:
        break

    if computer_score == 3:
        break

print()
print("Game Over! Final scores: ")
print("You {}, Me {}".format(player_score, computer_score))

print()
print("Game Over! Final scores: ")
print("You {}, Me {}".format(player_score, computer_score))

if computer_score > player_score:
    print("Better luck next time, I win!")

if player_score > computer_score:
    print("Congratulations, you have won!")





















