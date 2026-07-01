# Function to take input from user and return the number
def get_number():
    return int(input("Enter a number (0 to stop): "))

# Function to check if number is even
def is_even(num):
    return num % 2 == 0

# Function to calculate power with default exponent = 2
def power(base, exp=2):
    return base ** exp

# Function to show result (even/odd and square)
def show_result(num):
    if is_even(num):
        print(num, "is Even")
    else:
        print(num, "is Odd")
    print("Square of", num, "is:", power(num))   # default exponent = 2

# Main program using while loop
while True:
    n = get_number()
    if n == 0:   # stopping condition
        print("Program ended.")
        break
    show_result(n)
# Note:
# - get_number() handles user input.
# - is_even() checks even/odd.
# - power() demonstrates default parameter.
# - show_result() combines logic and prints results.
# - while loop repeats until user enters 0.
# - Recursion can be used for small parts if needed,
#   but here loop is sufficient for repeated input.
