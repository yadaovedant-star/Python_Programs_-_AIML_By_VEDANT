import numpy as np

# Create a 2D array of shape (10 students × 5 subjects) with random marks between 30 and 100
marks = np.random.randint(30, 101, (10, 5))
print("Student Marks Array:\n", marks)

# For each student, calculate total marks and average
total_marks = np.sum(marks, axis=1)
average_marks = np.mean(marks, axis=1)
print("Total Marks of Each Student:", total_marks)
print("Average Marks of Each Student:", average_marks)

# Find the student with highest and lowest total marks
highest_student = np.argmax(total_marks)
lowest_student = np.argmin(total_marks)
print("Student with Highest Total Marks (Index):", highest_student)
print("Student with Lowest Total Marks (Index):", lowest_student)

# Calculate overall class mean and standard deviation
print("Overall Class Mean:", np.mean(marks))
print("Overall Class Standard Deviation:", np.std(marks))

# Demonstrate indexing: Extract marks of top 3 students based on total marks
top3_indices = np.argsort(total_marks)[-3:]   # indices of top 3 students
print("Marks of Top 3 Students:\n", marks[top3_indices])

# Comments:
# - Generated random marks for 10 students in 5 subjects.
# - Calculated each student's total and average.
# - Found highest and lowest scoring students using argmax/argmin.
# - calculated overall class statistics.
# - Used indexing to extract marks of top 3 students.
