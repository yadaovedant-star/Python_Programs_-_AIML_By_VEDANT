#a) Creates one variable of each core data type: str, int, float, and bool.

SchoolName="Government polytechnic,Washim"
Semester=5
Cgpa=8.5
Student=True

#b) Prints each variable along with its data type using type().
print("My School Name is: ", SchoolName)
print(type(SchoolName))

print("My Semester is: ", Semester)
print(type(Semester))

print("My Cgpa is: ", Cgpa)
print(type(Cgpa))

print("Am I a Student? ", Student)
print(type(Student))

#c)Converting the integer to float and float to integer. Print the results and explain the output.

semester_into_float=float(Semester)
print("Semester into float is: ", semester_into_float)
#semester value was 5 which is an integer, after converting it into float it becomes 5.0 because float data type can hold decimal values.

cgpa_into_int=int(Cgpa)
print("Cgpa into int is: ", cgpa_into_int)
#cgpa value was 8.5 which is a float, after converting it into integer it becomes 8 because integer data type can only hold whole numbers 
# and it Removes the decimal part.