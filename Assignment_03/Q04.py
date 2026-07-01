# Defining a function that takes two numbers and returns their sum
def calculate_sum(a, b):
    return a + b   # using return 

# storing the result in a variable
result = calculate_sum(10, 20)

# Printing the result stored in the variable

print("Sum using return:", result)

# Demonstrating print() inside the function
def calculate_sum_print(a, b):
    print("Sum using print:", a + b)   # directly prints inside function

# Calling the function 
calculate_sum_print(10, 20)

# Difference:
# - return: Stores value In a variable For later use
# - print(): only displays the value
