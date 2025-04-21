def main():
    # Ask the user for an initial number
    curr_value = int(input("Enter a number: "))

    # Double the value until it's 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

# Boilerplate to call the main function
if __name__ == '__main__':
    main()
