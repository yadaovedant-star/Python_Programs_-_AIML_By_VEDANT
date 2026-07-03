import numpy as np

# Create the array
H1 = np.array([[10, 20, 30, 40],
               [50, 60, 70, 80],
               [90, 100, 110, 120]])
print("Array H1:\n", H1)

# Extract first row
print("First Row of H1:", H1[0])

# Extract last column
print("Last Column of H1:", H1[:, -1])

# Extract center 2x2 submatrix
print("Center 2x2 Submatrix of H1:\n", H1[1:3, 1:3])

# Extract all even numbers using boolean indexing
print("All Even Numbers in H1:", H1[H1 % 2 == 0])
