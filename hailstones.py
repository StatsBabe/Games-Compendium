"""
File: hailstones.py
-------------------
Aim: Also known as the Collatz or Syracuse hypothesis.
Input any positive random number. If it is even, it will be halved, if it is odd, it will be multiplied by 3, and 1 added.
The sequence will always end up at 1. Upper limit is defined as 100 to save programming time, but this constant can be changed.
Computer gives how many steps it took to get to 1.
"""
# define maximum value of the number to be input (=100), can be changed but will take more processing time
# define maximum value of the numbers in the steps (again to limit processing time) as n = 1000

MAX_VALUE = 100
MIN_VALUE = 1
# define the Hailstone/Collatz procedure
def Hailstone(n):
    workingvalue = 0
    if(n % 2 == 0):
        return (n//2)
    else:
        return (n*3+1)

def main():
    steps = 0
    workingvalue = int(input("Enter a number between " +str(MIN_VALUE)+ "and " +str(MAX_VALUE)+ ": "))
    while(workingvalue != 1):
        steps += 1
        print(int(workingvalue))
        workingvalue = Hailstone(workingvalue)
    print(workingvalue)

    print("Game is complete. This process took " +str(steps)+ " steps to get to number 1.")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
