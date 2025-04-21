def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create an empty phonebook

    while True:
        name = input("Name: ")  # Prompt user for a name
        if name == "":  # If no name is entered, stop the loop
            break
        number = input("Number: ")  # Prompt user for a phone number
        phonebook[name] = number  # Add the name and number to the dictionary

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))  # Print each name and associated number


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")  # Prompt user for a name to search for
        if name == "":  # If no name is entered, stop the loop
            break
        if name not in phonebook:  # If name is not found in phonebook
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])  # Print the associated phone number


def main():
    phonebook = read_phone_numbers()  # Create phonebook by reading user input
    print_phonebook(phonebook)  # Print the entire phonebook
    lookup_numbers(phonebook)  # Allow user to lookup numbers in the phonebook


# Python boilerplate.
if __name__ == '__main__':
    main()
