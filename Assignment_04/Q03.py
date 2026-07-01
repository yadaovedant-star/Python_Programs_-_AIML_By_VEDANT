# Q3. For Loop Revision

# a) Print all numbers from 1 to 25
print("Numbers from 1 to 25:")
for i in range(1, 26):   # generates numbers from 1 to 25
    print(i, end=' ')  # prints numbers on the same line separated by space
print("\n") #skips line 

# b) Print the sum of all numbers from 1 to 20
sum_numbers = 0
for i in range(1, 21):    # generates numbers 1 to 20
    sum_numbers += i      # adds number to sum_numbers
print("Sum of numbers from 1 to 20:", sum_numbers)


# c) Print the table of 5 from 5 × 1 to 5 × 10
print("Table of 5:")
for i in range(1, 11):    # generates numbers 1 to 10
    print("5 x", i, "=", 5 * i)
