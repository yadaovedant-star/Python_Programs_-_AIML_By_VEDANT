import numpy as np

# Create matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Matrix addition
sum_of_mat = A + B

# Matrix multiplication (two ways)
prod_of_mat_at = A @ B
prod_of_mat_dot = np.dot(A, B)

# Element-wise multiplication
elem_wise_mul = A * B

# Print with clear headings
print("Matrix A:\n", A)
print("Matrix B:\n", B)

print("\nMatrix Addition (A + B):\n", sum_of_mat)
print("Shape:", sum_of_mat.shape, " | Dtype:", sum_of_mat.dtype)

print("\nMatrix Multiplication using @ (A @ B):\n", prod_of_mat_at)
print("Matrix Multiplication using np.dot (np.dot(A, B)):\n", prod_of_mat_dot)
print("Shape:", prod_of_mat_at.shape, " | Dtype:", prod_of_mat_at.dtype)

print("\nElement-wise Multiplication (A * B):\n", elem_wise_mul)
print("Shape:", elem_wise_mul.shape, " | Dtype:", elem_wise_mul.dtype)
