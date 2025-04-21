def main():
    lst = []  # Create an empty list to store the user's inputs

    val = input("Enter a value: ")  # Prompt for the first value
    while val:  # Keep asking for input while the user provides a value
        lst.append(val)  # Add the entered value to the list
        val = input("Enter a value: ")  # Ask for the next value

    print("Here's the list:", lst)  # Print the final list when the user presses enter without typing anything


# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
