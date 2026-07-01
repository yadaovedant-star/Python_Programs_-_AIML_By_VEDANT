# Q4. OOP + Lists + Exception Handling
# Program: Student class with marks list and exception handling

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []  # empty list for marks

    def add_mark(self, mark):
        try:
            # ensure mark is numeric
            mark = int(mark)
            self.marks_list.append(mark)
        except ValueError:
            print("Invalid mark! Please enter a number.")

    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    def display_info(self):
        print("\n--- Student Information ---")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks List: {self.marks_list}")
        print(f"Average Marks: {self.get_average():.2f}")
        if self.marks_list:
            print(f"Highest Marks: {max(self.marks_list)}")
            print(f"Lowest Marks: {min(self.marks_list)}")
            print(f"Marks (Descending): {sorted(self.marks_list, reverse=True)}")


# Demonstration
student1 = Student("Vedant", 23)

# Input marks with exception handling
for i in range(5):
    mark = input(f"Enter marks for subject {i+1}: ")
    student1.add_mark(mark)

# Show all details
student1.display_info()