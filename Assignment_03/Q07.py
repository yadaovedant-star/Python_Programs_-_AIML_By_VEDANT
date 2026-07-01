# Recursive function to print numbers from n down to 1
def countdown(n):
    if n == 0:   # base case (stopping condition)
        return
    else:
        print(n)
        countdown(n - 1)   # recursive call with n-1

# Calling the function with 10
countdown(10)

# Note:
# Base case prevents infinite recursion.
# Each recursive call reduces n by 1 until it reaches 0.
