import numpy as np

# Create a 5x5 matrix of random integers between 1 and 100
S1 = np.random.randint(1, 101, (5, 5))
print("Matrix S1:\n", S1)

# Print diagonal elements
print("Diagonal Elements of S1:", np.diag(S1))

# Print elements greater than 50
print("Elements > 50 in S1:", S1[S1 > 50])

# Replace all elements less than 30 with 0
S1[S1 < 30] = 0

# Print the modified array
print("Modified Matrix S1:\n", S1)
