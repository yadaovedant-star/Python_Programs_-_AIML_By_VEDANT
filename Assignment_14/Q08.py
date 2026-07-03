import numpy as np

# Create two 3x3 matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Element-wise multiplication
print("Element-wise Multiplication (A * B):\n", A * B)

# Matrix multiplication
print("Matrix Multiplication (A @ B):\n", A @ B)
print("Matrix Multiplication using np.dot(A, B):\n", np.dot(A, B))


#Element-wise multiplication multiplies each element of A with the corresponding element of B.
# Matrix multiplication follows linear algebra rules: row of A multiplied with column of B.