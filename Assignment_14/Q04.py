import numpy as np

# Create 1D array from 1 to 24
arr = np.arange(1, 25)
print("Original Array:", arr)

# Reshape into 4x6
arr_4x6 = arr.reshape(4, 6)
print("Reshaped Array (4x6):\n", arr_4x6)
print("Shape:", arr_4x6.shape)

# Reshape into 3x8
arr_3x8 = arr.reshape(3, 8)
print("Reshaped Array (3x8):\n", arr_3x8)
print("Shape:", arr_3x8.shape)

# Reshape into 2x3x4 (3D array)
arr_2x3x4 = arr.reshape(2, 3, 4)
print("Reshaped Array (2x3x4):\n", arr_2x3x4)
print("Shape:", arr_2x3x4.shape)
