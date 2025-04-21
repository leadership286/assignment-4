def add_many_numbers(numbers) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number  # Add each number to the total
    
    return total_so_far  # Return the final sum

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # Example list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum

if __name__ == '__main__':
    main()
