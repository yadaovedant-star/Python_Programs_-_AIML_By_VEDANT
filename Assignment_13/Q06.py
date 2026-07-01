import numpy as np

# Create vectors
v1 = np.array([2, 4, 6, 8])
v2 = np.array([1, 3, 5, 7])

# a) Addition
add_of_result = v1 + v2

# b) Subtraction
sub_of_result = v1 - v2

# c) Element-wise multiplication
mul_of_result = v1 * v2

# d) Dot product
dot_of_result = np.dot(v1, v2)

# Printing results
print("Vector v1:", v1)
print("Vector v2:", v2)

print("\nAddition (v1 + v2):\n", add_of_result)
print("Subtraction (v1 - v2):\n", sub_of_result)
print("Element-wise Multiplication (v1 * v2):\n", mul_of_result)
print("Dot Product (v1 . v2):\n", dot_of_result)

