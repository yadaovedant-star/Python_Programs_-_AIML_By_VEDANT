# Q6. Program to keep adding positive numbers until user enters 0 or negative

# Start with total sum as 0
total = 0   # running total of all positive numbers

# Ask the user for the first number
num = int(input("Enter a positive number (0 or negative to stop): "))

# Keep looping while the number is positive
while num > 0:   # condition check
    total += num   # add the number to total
    # Ask again for the next number
    num = int(input("Enter a positive number (0 or negative to stop): "))

# Loop ends when user enters 0 or negative
print("Total sum of entered positive numbers:", total)
