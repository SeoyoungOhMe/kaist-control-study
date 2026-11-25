
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
T = 10
target = 10

t = np.arange(0, T, dt)

def simulate_p(Kp):
    x = np.zeros(len(t))

    for i in range(len(t) - 1):
        # 1. 오차 계산
        error = target - x[i]

        # 2. P 제어 입력 계산
        u = Kp * error

        # 3. 시스템의 상태 변화율 계산
        dx = -x[i] + u

        # 4. Euler 적분
        x[i + 1] = x[i] + dx * dt

    return x

for Kp in [0.5, 1, 2, 5, 10]:
    x = simulate_p(Kp)
    plt.plot(t, x, label=f"Kp={Kp}")

plt.axhline(target, color="black", linestyle="--",
            label="Target")

plt.xlabel("Time (s)")
plt.ylabel("State")
plt.legend()
plt.grid()
plt.show()
