import random

def main():
    # Generate a random number between 1 and 99
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")

    # Ask the user to make their first guess
    guess = int(input("Enter a guess: "))

    # Keep asking until they get it right
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Just to make the output prettier
        guess = int(input("Enter a new guess: "))

    print("Congrats! The number was:", secret_number)

if __name__ == '__main__':
    main()
