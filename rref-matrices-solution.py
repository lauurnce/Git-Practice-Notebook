import numpy as np
from sympy import Matrix

# Example 5x5 coefficient matrix (A) and right-hand side vector (b)
A = np.array([
    [2, 1, 3, 4, 5],
    [1, 2, 1, 3, 4],
    [3, 1, 2, 1, 2],
    [4, 3, 1, 2, 1],
    [5, 4, 2, 1, 2]
], dtype=float)

b = np.array([10, 8, 7, 6, 5], dtype=float)

# Form augmented matrix [A | b]
aug = np.column_stack((A, b))

# Use sympy to compute RREF
rref_matrix, pivots = Matrix(aug).rref()

print("Reduced Row Echelon Form (RREF):")
print(np.array(rref_matrix, dtype=float))

# Extract solution if unique
solution = np.array(rref_matrix[:, -1], dtype=float)
print("Solution vector x:")
print(solution)