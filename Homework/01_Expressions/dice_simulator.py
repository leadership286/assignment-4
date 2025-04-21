"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.
Prints the results of each die roll.
This program is used to show how variable scope works.
"""

import random

# Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print("Total of two dice:", total)

def main():
    die1 = 10  # This is a variable defined in main(), not the roll_dice() function
    print("die1 in main() starts as: " + str(die1))

    roll_dice()
    roll_dice()
    roll_dice()

    print("die1 in main() is: " + str(die1))

# Call the main() function
if __name__ == '__main__':
    main()
