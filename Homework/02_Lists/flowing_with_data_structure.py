def add_three_copies(my_list, data):
    # Adds the data three times to the list
    for i in range(3):
        my_list.append(data)

########## No need to edit code past this point

def main():
    # Take user input for the message to copy
    message = input("Enter a message to copy: ")
    
    # Initialize an empty list
    my_list = []
    
    # Print the list before adding copies
    print("List before:", my_list)
    
    # Call the function to add three copies of the message to the list
    add_three_copies(my_list, message)
    
    # Print the list after the changes
    print("List after:", my_list)

if __name__ == "__main__":
    main()
