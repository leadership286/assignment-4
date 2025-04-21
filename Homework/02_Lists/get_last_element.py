def get_last_element(lst):
    """
    Prints the last element of the provided list.
    """
    print(lst[-1])  # This is the simplest way to get the last element in Python

# The line below works as well:
# print(lst[len(lst) - 1])

# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":  # While user keeps entering non-empty input
        lst.append(elem)  # Add the element to the list
        elem = input("Please enter an element of the list or press enter to stop. ")  # Ask for the next element
    return lst

def main():
    lst = get_lst()  # Get the list from user input
    get_last_element(lst)  # Print the last element of the list

if __name__ == '__main__':
    main()
