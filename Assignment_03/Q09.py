# Global variable
total = 0

# Function to add value to global variable
def add_value(x):
    global total   # declare that we are using the global variable
    total += x
    print("Total after adding", x, ":", total)

# Calling the function multiple times
add_value(5)
add_value(10)
add_value(20)

# Demonstrating local variable scope
def demo_scope():
    local_var = 100
    print("Inside function, local_var =", local_var)

demo_scope()

# Trying to access local_var outside the function will cause an error
# print(local_var)   # Uncommenting this line will give: NameError: name 'local_var' is not defined

# Note:
# - Global variables can be accessed and modified across functions using 'global' keyword.
# - Local variables exist only inside the function and cannot be accessed outside.
