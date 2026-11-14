import numpy as np

m = 1.0
k = 4.0
c = 1.0

A = np.array([
    [0, 1],
    [-k/m, -c/m]
])

B = np.array([
    [0],
    [1/m]
])

# Controllability matrix
C = np.hstack((B, A @ B))

rank = np.linalg.matrix_rank(C)

print("Controllability matrix:")
print(C)

print("Rank:", rank)

print("Controllable:", rank == A.shape[0])