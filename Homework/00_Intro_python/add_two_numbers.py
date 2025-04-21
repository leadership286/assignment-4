"""
Program: add2numbers
--------------------
A simple Python program to practice with
variables and input/output. This program 
asks the user for two integers and prints their sum.
"""

def main():
    print("This program adds two numbers.")
    
    # Getting first number
    num1 = int(input("Enter the first number: "))
    
    # Getting second number
    num2 = int(input("Enter the second number: "))
    
    # Calculating the sum
    total = num1 + num2
    
    # Displaying the result
    print("The total is " + str(total) + ".")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
