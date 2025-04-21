import random

N_NUMBERS = 10  # Number of random numbers to generate
MIN_VALUE = 1  # Minimum value for the random number
MAX_VALUE = 100  # Maximum value for the random number

def main():
    # Generate and print 10 random numbers between 1 and 100
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=' ')

if __name__ == '__main__':
    main()

