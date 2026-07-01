# While Loop Revision

total = 0
num = int(input("Enter a positive number (0 or negative to stop): "))

while num > 0:
    total += num
    num = int(input("Enter a positive number (0 or negative to stop): "))

print("Total sum of entered positive numbers:", total)
