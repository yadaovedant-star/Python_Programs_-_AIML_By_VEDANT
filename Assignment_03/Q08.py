# Recursive function to calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:   # base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial(n - 1)   # recursive call with n-1

# Taking input from user
num = int(input("Enter a number: "))

# Calling the recursive function and storing result
result = factorial(num)

# Printing the result
print("Factorial of", num, "is:", result)

# Note:
# Base case is important because it stops recursion.
# Without the base case, the function would call itself infinitely.
