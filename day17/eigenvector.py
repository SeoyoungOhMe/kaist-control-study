
import numpy as np
import matplotlib.pyplot as plt

m, k = 1.0, 4.0

for c in [0, 2, 4, 6]:
    A = np.array([
        [0, 1],
        [-k/m, -c/m]
    ])
    eigvals = np.linalg.eigvals(A)

    plt.scatter(eigvals.real, eigvals.imag,
                label=f"c={c}", s=70)

plt.axvline(0, linestyle="--")
plt.axhline(0, linestyle=":")
plt.xlabel("Real part")
plt.ylabel("Imaginary part")
plt.title("Eigenvalues on Complex Plane")
plt.legend()
plt.grid()
plt.show()
