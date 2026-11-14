# Example: uncontrollable system
import numpy as np

m = 1.0
k = 4.0
c = 1.0

A = np.array([
    [-1, 0],
    [0, -2]
])

B = np.array([
    [1],
    [0]
])

C = np.hstack((B, A @ B))

print(C)
print("Rank:", np.linalg.matrix_rank(C))