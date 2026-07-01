# Lambda function to add three numbers
Add_Three = lambda a, b, c: a + b + c   # lambda creates a one-line anonymous function

# Take three inputs from user
a = int(input("Enter first number: "))#input 1
b = int(input("Enter second number: "))#input 2
c = int(input("Enter third number: "))#input 3

# Call lambda function and print result
print("Sum of three numbers is:", Add_Three(a, b, c))
