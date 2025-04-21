import random

# Constants
PROMPT: str = "What do you want? "
SORRY: str = "Sorry I only tell jokes."

# List of jokes
JOKES = [
    "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'.",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the JavaScript developer go broke? Because he kept using 'var' when he should have been using 'let'!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
    "Why did the Python programmer go on a diet? Because he couldn't 'import' self-control!",
    "Why do computers always sing? Because they have good 'bytes'.",
    "A user interface is like a joke. If you have to explain it, it’s not that good."
]

def main():
    # Ask the user what they want
    user_input = input(PROMPT)

    # Check the user's response
    if user_input == "Joke":
        # Choose a random joke from the list
        joke = random.choice(JOKES)
        print(joke)
    else:
        print(SORRY)

# Run the main function
if __name__ == "__main__":
    main()
