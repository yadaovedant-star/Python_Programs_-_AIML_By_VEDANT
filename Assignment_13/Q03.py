import numpy as np

# a) Numbers from 0 to 20 (step 1)
N1 = np.arange(0, 21, 1)

# b) Even numbers from 10 to 50
N2 = np.arange(10, 51, 2)

# c) Numbers from 5 to 100 with step of 5
N3 = np.arange(5, 101, 5)

# Printing with labels
print("Array N1 (0 to 20 step 1):\n", N1)
print("Shape:", N1.shape, " | Data Type:", N1.dtype)

print("\nArray N2 (Even numbers 10 to 50):\n", N2)
print("Shape:", N2.shape, " | Data Type:", N2.dtype)

print("\nArray N3 (5 to 100 step 5):\n", N3)
print("Shape:", N3.shape, " | Data Type:", N3.dtype)
