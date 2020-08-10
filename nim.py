"""
File: nimm.py
-------------------------
Aim: there are 20 stones and each player will pick either 1 or 2 stones alternately. Winner does not pick last stone.
Pre-condition: a pile of 20 stones and 2 players who will pick either 1 or 2 stones alternately
Post_condition: all stones have been picked up. Loser is person who does not have to pick the last stone
"""
# initial state is a pile of 20 stones
state = 20

def main():
    print("Game is over. Hope you enjoyed it!")

print("Welcome to the ancient game of Nim. You are player 1, computer is player 2.")
print("Two players alternate taking either 1 or 2 stones from the pile of " +str(state)+ ".")
print("To make it easier for you to win, please choose on behalf of the computer.")
print("The winner is the player who does not pick the last stone.")
# set player to 1
player = 1
while True:
    # get move
    print("Player ", player)
    while True:
        move = int(input("Please say whether you have taken 1 or 2 stones from the pile: "))
        if move in [1,2] and move<state:
            break
        print ("You cannot make that move.")

    #update the state
    state=state-move
    # show the state
    print("There are now " +str(state)+ " stones left.")

    # check win/lose state
    if state == 1:
        print("Well done the winner, player ", player)
        break

    # switch players, 1->2, 2->1
    if player == 1:
        player = 2
    else:
        player = 1

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()