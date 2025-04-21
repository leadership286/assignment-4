# Import the random library to simulate random events like rolling dice
import random

# Number of sides on each die to roll
NUM_SIDES: int = 6

def main():
    # Roll two dice (random integers between 1 and NUM_SIDES)
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    
    # Get the total of the dice
    total: int = die1 + die2
    
    # Print out the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)


# This provided line is required at the end of the Python file
# to call the main() function.
if __name__ == '__main__':
    main()
