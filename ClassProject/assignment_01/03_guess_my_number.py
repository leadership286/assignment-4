import random

def main():
    # Generate the secret number at random between 0 and 99
    secret_number: int = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    # Get user's initial guess
    guess = int(input("Enter a guess: "))
    
    # Keep asking the user for a guess until they guess the correct number
    while guess != secret_number:
        if guess < secret_number:  # If guess is lower than the secret number
            print("Your guess is too low")
        else:  # If guess is higher than the secret number
            print("Your guess is too high")
        
        # Ask the user for a new guess
        guess = int(input("Enter a new guess: "))
    
    # Once the correct number is guessed, congratulate the user
    print("Congrats! The number was: " + str(secret_number))

# Call the main function when the script is run
if __name__ == '__main__':
    main()
