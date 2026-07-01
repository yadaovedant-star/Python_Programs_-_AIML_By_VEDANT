import numpy as np

# a) Generate a 1D array of 20 random integers between 1 and 50
D1_Array = np.random.randint(1, 51, 20)

# b) Reshape into a 4x5 matrix
matrix = D1_Array.reshape(4, 5)

# c) Statistics
total_sum = matrix.sum()
mean_val = matrix.mean()
std_dev = matrix.std()

# d) Maximum value in each row
row_max = matrix.max(axis=1)

# Printing results
print("Q9 - 1D Array (20 random integers 1 to 50):\n", D1_Array)
print("\nQ9 - Reshaped Matrix (4x5):\n", matrix)

print("\nSum of all elements:", total_sum)
print("Mean of matrix:", mean_val)
print("Standard Deviation:", std_dev)

print("\nMaximum value in each row:", row_max)


