# Defining a function with two parameters: name and age
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

# Calling the function using positional arguments
student_info("Vedant", 20)
student_info("Chinmay", 19)
# Calling the function using keyword arguments
student_info(name="sarthak", age=18)
student_info(name="Sanika", age=20)
# Difference:
# - Positional arguments: values are passed in the same order as parameters
# - Keyword arguments: values are passed by naming the parameter
#   so order does not matter and code is more readable.
