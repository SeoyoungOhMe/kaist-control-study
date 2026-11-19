
import numpy as np
import matplotlib.pyplot as plt

m, c = 1.0, 2.0

for k in [1, 4, 9]:
    A = np.array([
        [0, 1],
        [-k/m, -c/m]
    ])
    print(f"k={k}: {np.linalg.eigvals(A)}")
