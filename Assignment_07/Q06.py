# Tuple containing student information
student = ('Rahul', 20, 'Computer Science', 'A')

# a) Iterate through the tuple using a for loop
print("Iterating through the tuple:")
for item in student:
    print(item)

# b) Unpack the tuple into four variables
name, age, branch, grade = student

print("\nUnpacked Values:")
print("Name:", name)
print("Age:", age)
print("Branch:", branch)
print("Grade:", grade)
