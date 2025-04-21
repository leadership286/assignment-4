
MAX_LENGTH: int = 3  # Define the maximum allowed length for the list

def shorten(lst):
    # Keep removing items from the end of the list until it reaches MAX_LENGTH
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Remove the last element from the list
        print(last_elem)  # Print the removed element

# Helper function to get a list from the user input
def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)  # Add the entered element to the list
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  # Get the list from the user
    shorten(lst)  # Call shorten to modify the list

if __name__ == '__main__':
    main()  # Run the program

