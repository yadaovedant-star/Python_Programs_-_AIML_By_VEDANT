# Tuple of grades
grades = ('A', 'B', 'A', 'C', 'A', 'B', 'D', 'A', 'B')

# Count occurrences of 'A' and 'B'
print("Count of 'A':", grades.count('A'))
print("Count of 'B':", grades.count('B'))

# Take a grade as input from the user
grade_input = input("Enter a grade to count: ")

# Print how many times it appears
print("Count of", grade_input, ":", grades.count(grade_input))
