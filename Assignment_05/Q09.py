# a) First 10 even numbers (2 to 20)
print("First 10 even numbers (2 to 20):")
for i in range(2, 21, 2):   # start=2, stop=21, step=2 → evens
    print(i, end=" ")
print("\n")

# b) Numbers from 1 to 30 in steps of 3
print("Numbers from 1 to 30 in steps of 3:")
for i in range(1, 31, 3):   # start=1, stop=31, step=3
    print(i, end=" ")
print("\n")
# c) String slicing example BELOW
text = "PythonProgramming"

# Slice "Python" → first 6 characters
print("Slice 1:", text[0:6])

# Slice "Programming" → from index 6 till end
print("Slice 2:", text[6:])

# Reverse the string using slicing
print("Reverse:", text[::-1])
