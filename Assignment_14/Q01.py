import numpy as np

# Create a 2D array of shape (5, 6) filled with random integers between 10 and 100
V1 = np.random.randint(10, 101, (5, 6))

# Print the array
print("Q1 - 2D Array (5x6 random integers 10 to 100):\n", V1)

# Print properties
print("\nShape of the array:", V1.shape)
print("Total number of elements (size):", V1.size)
print("Data type (dtype):", V1.dtype)
print("Number of dimensions:", V1.ndim)