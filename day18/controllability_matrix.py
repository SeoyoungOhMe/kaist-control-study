import numpy as np

A = np.array([[0, 1],
              [0, 0]])

B = np.array([[0],
              [1]])

C = np.hstack((B, A @ B))

print("Controllability Matrix:\n", C)
print("Rank:", np.linalg.matrix_rank(C))