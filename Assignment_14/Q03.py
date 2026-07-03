import numpy as np

# Create a 4x5 matrix of random integers between 20 and 80
G1 = np.random.randint(20, 81, (4, 5))
print("Matrix G1:\n", G1)

# Minimum and maximum value
print("Minimum Value in G1:", np.min(G1))
print("Maximum Value in G1:", np.max(G1))

# Sum of all elements
print("Sum of Elements in G1:", np.sum(G1))

# Mean and Standard Deviation
print("Mean of G1:", np.mean(G1))
print("Standard Deviation of G1:", np.std(G1))

# Sum of each row
print("Row-wise Sum of G1:", np.sum(G1, axis=1))

# Sum of each column
print("Column-wise Sum of G1:", np.sum(G1, axis=0))
