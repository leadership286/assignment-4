MAX_TERM_VALUE = 10000  # Constant value for the upper limit of the sequence

def main():
    curr_term = 0  # The 0th Fibonacci number
    next_term = 1  # The 1st Fibonacci number

    # Loop as long as the current term is within the allowed max
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Print all on the same line, separated by spaces
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

if __name__ == '__main__':
    main()
