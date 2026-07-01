# Q10. Student Record Program using Tuples

# --- Step 1: Take input and pack into a tuple ---
name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
mark1 = int(input("Enter marks for Subject 1: "))
mark2 = int(input("Enter marks for Subject 2: "))
mark3 = int(input("Enter marks for Subject 3: "))

# Tuple Packing → storing all info in one tuple
student_record = (name, roll, mark1, mark2, mark3)

# --- Step 2: Print complete record ---
print("\nComplete Student Record:", student_record)

# --- Step 3: Unpack tuple into variables ---
name, roll, mark1, mark2, mark3 = student_record
print("\nUnpacked Values:")
print("Name:", name)
print("Roll Number:", roll)
print("Subject 1 Marks:", mark1)
print("Subject 2 Marks:", mark2)
print("Subject 3 Marks:", mark3)

# --- Step 4: Use count() to check frequency of a mark ---
mark_input = int(input("\nEnter a mark to check frequency: "))
print("The mark", mark_input, "appears", student_record.count(mark_input), "time(s).")

# --- Step 5: Nested tuple for multiple student records ---
student1 = student_record
student2 = ("sarthak", 134, 84, 78, 90)   # another student record
students = (student1, student2)         # nested tuple

print("\nNested Student Records:", students)

# Access specific values
print("Second student's name:", students[1][0])         # Rahul
print("First student's Subject 2 marks:", students[0][3])  # mark2 of first student
