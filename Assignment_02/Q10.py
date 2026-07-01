# Debugging Program

# FIX 1: input() returns string, so convert to int for numeric comparison
num = int(input("Enter a number: "))

# FIX 2: Missing colon (:) after if condition
if num > 100:
    print("Large number")

# FIX 3: Missing colon (:) after elif condition
elif num > 50:
    print("Medium number")

# FIX 4: Missing colon (:) after else
else:
    print("Small number")

# FIX 5: Initialize counter correctly
count = 1

# FIX 6: Missing colon (:) after while condition
while count < 10:
    print(count)
    # FIX 7: count + 1 does not change value, must use += to increment
    count += 1
