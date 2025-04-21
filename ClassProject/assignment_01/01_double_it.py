def main():
    # Ask the user to input a number
    curr_value = int(input("Enter a number: "))

    # Continue doubling the number while it's less than 100
    while curr_value < 100:
        curr_value *= 2
        print(curr_value, end=" ")

# This line will ensure that the main function is executed when the program is run
if __name__ == '__main__':
    main()
