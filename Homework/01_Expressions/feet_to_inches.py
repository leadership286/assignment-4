# Conversion factor constant
INCHES_IN_FOOT: int = 12  # There are 12 inches in 1 foot

def main():
    feet: float = float(input("Enter number of feet: "))  # Get the number of feet, make sure to cast it to a float!
    inches: float = feet * INCHES_IN_FOOT  # Perform the conversion
    print("That is", inches, "inches!")  # Output the result
    
    
# This provided line is required at the end of the Python file
# to call the main() function.
if __name__ == '__main__':
    main()
