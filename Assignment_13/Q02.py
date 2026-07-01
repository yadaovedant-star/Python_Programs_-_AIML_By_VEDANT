import numpy as np

# a) 1D array of 8 zeros
V1 = np.zeros(8)

# b) 2D array (4x4) filled with ones
V2 = np.ones((4, 4))

# c) 3x3 matrix of zeros
V3 = np.zeros((3, 3))

# Printing with labels
print("Array V1 (1D zeros):\n", V1)
print("Shape:", V1.shape, " | Data Type:", V1.dtype)

print("\nArray V2 (4x4 ones):\n", V2)
print("Shape:", V2.shape, " | Data Type:", V2.dtype)

print("\nArray V3 (3x3 zeros):\n", V3)
print("Shape:", V3.shape, " | Data Type:", V3.dtype)


