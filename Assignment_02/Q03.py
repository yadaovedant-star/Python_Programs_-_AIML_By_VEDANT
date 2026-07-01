# Q3. Program to assign grades based on marks

# Ask the user to enter marks
marks = int(input("Enter your marks: "))   # convert input string to integer

# Check conditions using if-elif-else ladder
if marks >= 90:   # condition for Grade A
    print("Grade A  Excellent")
elif marks >= 75:   # condition for Grade B
    print("Grade B  Good")
elif marks >= 60:   # condition for Grade C
    print("Grade C  Average")
elif marks >= 40:   # condition for Grade D
    print("Grade D  Pass")
else:   # condition for marks less than 40
    print("Fail")
