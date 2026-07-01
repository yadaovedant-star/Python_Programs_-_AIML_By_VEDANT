# Q5. Program to print numbers from 1 to 20 and their cubes using while loop

# Start with the first number
num = 1   # initialize variable

# Keep looping until num exceeds 20
while num <= 20:   # condition check
    # Print the number and its cube
    print("Number:", num, " Cube:", num ** 3)   # ** is exponent operator
    
    # Move to the next number
    num += 1   # increment by 1 each time

# Loop stops automatically when num becomes 21 (condition False)
