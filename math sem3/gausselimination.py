import numpy as np

# Get the number of equations and variables from the user
n = int(input("Enter the number of equations: "))
m = int(input("Enter the number of variables: "))

# Initialize empty coefficient matrix A and constants vector B
A = np.zeros((n, m), dtype=float)
B = np.zeros(n, dtype=float)

# Get the coefficients and constants from the user
print("Enter the coefficients for each equation:")
for i in range(n):
    for j in range(m):
        A[i, j] = float(input(f"A[{i+1}][{j+1}]: "))
    B[i] = float(input(f"Enter the constant for equation {i+1}: "))

# Combine the coefficient matrix A and constants B into one augmented matrix
augmented_matrix = np.column_stack((A, B))

# Perform Gaussian elimination to transform the augmented matrix into row-echelon form
for i in range(n):
    pivot = augmented_matrix[i, i]
    augmented_matrix[i, :] /= pivot
    for j in range(i + 1, n):
        factor = augmented_matrix[j, i]
        augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

# Back-substitution to find the solutions
x = np.zeros(n, dtype=float)
for i in range(n - 1, -1, -1):
    x[i] = augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:n], x[i+1:n])

# Print the solutions
print("Solution:")
print(x)
