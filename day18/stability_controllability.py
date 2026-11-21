import numpy as np

systems = {
    "①": (np.diag([-1, -2]), [[1], [1]]),
    "②": (np.diag([ 1, -2]), [[1], [1]]),
    "③": (np.diag([-1, -2]), [[1], [0]]),
    "④": (np.diag([ 1, -2]), [[0], [1]])
}

for name, (A, B) in systems.items():
    B = np.array(B)

    eig = np.linalg.eigvals(A)
    C = np.hstack((B, A @ B))
    rank = np.linalg.matrix_rank(C) # controllability

    stable = np.all(np.real(eig) < 0) # stability : 고유값의 실수부가 모두 음수
    controllable = (rank == 2)

    print(name, eig, stable, controllable)
