try:
    # Take input from user
    num_str = input("Enter a number: ")
    num = int(num_str)   # may raise ValueError

    # Perform division
    result = 100 / num   # may raise ZeroDivisionError
    print("Result is:", result)

except (ValueError, ZeroDivisionError):
    # Handles both invalid input and division by zero
    print("Error: Please enter a valid non-zero integer.")


