# Program: index() and count()

scores = [85, 92, 78, 92, 65, 92, 88]

# Find index of first occurrence of 92
print("Index of first 92:", scores.index(92))

# Count how many times 92 appears
print("Count of 92:", scores.count(92))

# Take user input
num = int(input("Enter a number to search: "))

if num in scores:
    print(num, "found at index:", scores.index(num))
    print(num, "appears", scores.count(num), "times")
else:
    print(num, "not found in the list")


