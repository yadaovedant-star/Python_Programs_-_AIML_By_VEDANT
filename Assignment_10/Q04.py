class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

    def show_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())
        print("-------------------")

student1 = Student("Ram", 81)
student2 = Student("Aavanti", 78)
student3 = Student("Prachi", 99)

student1.show_details()
student2.show_details()
student3.show_details()


