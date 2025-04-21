def main():
    # Dictionary of fruits and their prices
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0  # To keep track of the total bill

    # Loop through each fruit to ask the user how many they want
    for fruit_name in fruits:
        price = fruits[fruit_name]
        # Prompt user for quantity
        amount_bought = int(input(f"How many ({fruit_name}) do you want?: "))
        total_cost += price * amount_bought

    # Print the total cost
    print("Your total is $" + str(total_cost))


# Required boilerplate to run the program
if __name__ == '__main__':
    main()
