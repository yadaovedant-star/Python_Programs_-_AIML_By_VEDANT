# Q4. Nested Dictionary Example

# Creating a nested dictionary with two students
students = {
    "s1": {"name": "Rahul", "age": 20, "marks": 88},
    "s2": {"name": "Sneha", "age": 21, "marks": 95}
}

# Printing the details of the first student
print("First Student Details:", students["s1"])

# Printing the marks of the second student
print("Second Student Marks:", students["s2"]["marks"])

# Adding a new subject "math" with marks 90 for the first student
students["s1"]["math"] = 90

# Printing the updated dictionary
print("\nUpdated Students Dictionary:", students)


