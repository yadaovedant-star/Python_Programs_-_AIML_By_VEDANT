# Q1. Program to check voting eligibility
# Ask the user to enter their age
age = int(input("Enter your age: "))   # input() returns string, so convert to int

# If age is 18 or more, print eligibility message
if age >= 18:   # condition check
    print("You are eligible to vote.")   # executes only if condition is True

# If condition is False (age < 18), nothing will be printed