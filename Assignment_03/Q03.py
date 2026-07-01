# Defining a function with a default parameter 'message'
def show_message(message="Hello"):
    print(message)

# Calling the function without passing any argument (uses default value)
show_message()

# Calling the function again by passing a different message
show_message("Welcome to AIML Bro!")

# Benefit of default parameters:
# They provide a default value if no argument is passed
# making functions more flexible and reducing errors
