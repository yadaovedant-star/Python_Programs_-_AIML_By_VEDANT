import numpy as np

# Generate 1D array of 20 random integers between 1 and 50
V1 = np.random.randint(1, 51, 20)
print("Array:", V1)

# Minimum value and its index
print("Minimum Value:", np.min(V1))
print("Index of Minimum (argmin):", np.argmin(V1))

# Maximum value and its index
print("Maximum Value:", np.max(V1))
print("Index of Maximum (argmax):", np.argmax(V1))

# Sum of all elements
print("Sum of Elements:", np.sum(V1))

# Mean and Standard Deviation
print("Mean:", np.mean(V1))
print("Standard Deviation:", np.std(V1))

