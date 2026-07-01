# Function that returns the square of a number using exponentiation
def square(num):
    return num ** 2   # return sends the result back

# Function that returns the cube of a number using exponentiation
def cube(num):
    return num ** 3   # return sends the result back

# Main program: take input from user
n = int(input("Enter a number: "))

# Store results in variables using return values
sq = square(n)
cu = cube(n)

# Print the results
print("Square of", n, "is:", sq)
print("Cube of", n, "is:", cu)

# Note:
# Using return allows storing results in variables
# and reusing them later, unlike print() which only displays output.
