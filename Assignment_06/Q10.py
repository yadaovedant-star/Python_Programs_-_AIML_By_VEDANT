# Program: Student Marks Manager

# Take 5 subject marks from user
marks = []
for i in range(5):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

print("Marks list:", marks)

# Add one more subject mark
extra = int(input("Enter marks for extra subject: "))
marks.append(extra)
print("After adding extra subject:", marks)

# Highest and lowest marks
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))

# Sort in descending order
marks.sort(reverse=True)
print("Marks in descending order:", marks)

# Average marks
average = sum(marks) / len(marks)
print("Average marks:", round(average, 2))

# Total subjects
print("Total subjects:", len(marks))
