import numpy as np

# a) 1D array of 10 random numbers between 0 and 1
D1 = np.random.rand(10)

# b) 3x3 matrix of random numbers from standard normal distribution
D2 = np.random.randn(3, 3)

# c) 2D array (4x5) of random integers between 10 and 50
D3 = np.random.randint(10, 51, (4, 5))

# Printing with headings
print("Array D1 (10 random numbers between 0 and 1):\n", D1)
print("Shape:", D1.shape, " | Data Type:", D1.dtype)

print("\nArray D2 (3x3 matrix from standard normal distribution):\n", D2)
print("Shape:", D2.shape, " | Data Type:", D2.dtype)

print("\nArray D3 (4x5 random integers between 10 and 50):\n", D3)
print("Shape:", D3.shape, " | Data Type:", D3.dtype)

print("Code Executed Successfully Vedant")