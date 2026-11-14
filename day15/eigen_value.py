import numpy as np
import matplotlib.pyplot as plt

m = 1.0
k = 4.0
# c = 1.0

# A = np.array([
#     [0, 1],
#     [-k/m, -c/m]
# ])

# eigenvalues = np.linalg.eigvals(A)

# print("System matrix:")
# print(A)

# print("Eigenvalues:")
# print(eigenvalues)

for c in [0, 1, 4, 5]:
    A = np.array([
        [0, 1],
        [-k/m, -c/m]
    ])

    eigenvalues = np.linalg.eigvals(A)

    print(f"c={c}: {eigenvalues}")

for c in [0, 1, 4, 5]:
    A = np.array([
        [0, 1],
        [-4, -c]
    ])

    eig = np.linalg.eigvals(A)

    plt.scatter(eig.real, eig.imag, label=f"c={c}")

plt.axvline(0, linestyle="--")
plt.axhline(0, linestyle="--")
plt.xlabel("Real part")
plt.ylabel("Imaginary part")
plt.legend()
plt.grid()
plt.show()