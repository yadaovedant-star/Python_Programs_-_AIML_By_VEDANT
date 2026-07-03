import numpy as np

# Generate a 6x6 matrix of random numbers using np.random.randn()
M1 = np.random.randn(6, 6)
print("Matrix M1:\n", M1)

# Print shape, size, and dtype
print("Shape of M1:", M1.shape)
print("Size of M1:", M1.size)
print("Data Type of M1:", M1.dtype)

# Find index of maximum and minimum value
print("Index of Maximum Value in M1:", np.argmax(M1))
print("Index of Minimum Value in M1:", np.argmin(M1))

# Extract top-left 3x3 submatrix
print("Top-left 3x3 Submatrix of M1:\n", M1[0:3, 0:3])

# Replace all negative numbers with their absolute value
M1[M1 < 0] = np.abs(M1[M1 < 0])

# Print mean of modified matrix
print("Mean of Modified M1:", np.mean(M1))
