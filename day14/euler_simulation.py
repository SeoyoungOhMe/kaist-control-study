import numpy as np
import matplotlib.pyplot as plt

# 물리 파라미터
m = 1.0
k = 4.0
c = 0.4

# 초기 조건
x0 = 1.0
v0 = 0.0

# 전체 시뮬레이션 시간
T = 10.0

def simulate_euler(dt):
    n_steps = round(T / dt)

    t = np.linspace(0, T, n_steps + 1)
    x = np.zeros(n_steps + 1)
    v = np.zeros(n_steps + 1)

    x[0] = x0
    v[0] = v0

    for i in range(n_steps):
        a = (-k * x[i] - c * v[i]) / m

        x[i + 1] = x[i] + v[i] * dt
        v[i + 1] = v[i] + a * dt

    return t, x, v

for dt in [0.2, 0.05, 0.01]:
    t, x, v = simulate_euler(dt)

    plt.plot(t, x, label=f"dt={dt}s")

plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Euler Integration Comparison")
plt.legend()
plt.grid(True)
plt.show()