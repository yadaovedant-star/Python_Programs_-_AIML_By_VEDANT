#taking input from user for name, age, city and marks in 3 subjects
name=input("Enter your name: ")
age=int(input("Enter your age: "))
city=input("Enter your city: ")

#taking input for marks in 3 subjects
Marks_in_subject1=int(input("Enter marks in subject 1: "))
Marks_in_subject2=int(input("Enter marks in subject 2: "))
Marks_in_subject3=int(input("Enter marks in subject 3: "))

#calculating total marks and percentage
total_marks=Marks_in_subject1+Marks_in_subject2+Marks_in_subject3
percentage=(total_marks/300)*100

#printing the details of the student
print("----------\nStudent Details\n----------")
print("Your Name Is: ", name)
print("Your Age is: ", age)
print("Your City IS: ", city)
print("Percentage Obtained Is: ", percentage)