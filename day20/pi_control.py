
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
T = 20
target = 10

t = np.arange(0, T, dt)

def simulate_pi(Kp, Ki):
    x = np.zeros(len(t))
    integral = 0.0

    for i in range(len(t) - 1):
        error = target - x[i]

        # 오차 누적
        integral += error * dt

        # PI 제어 입력
        u = Kp * error + Ki * integral

        # 시스템의 상태 변화
        dx = -x[i] + u

        # Euler 적분
        x[i + 1] = x[i] + dx * dt

    return x

Kp = 2

for Ki in [0, 0.5, 1, 2, 5]:
    x = simulate_pi(Kp, Ki)
    plt.plot(t, x, label=f"Kp={Kp}, Ki={Ki}")

plt.axhline(target, color="black", linestyle="--",
            label="Target")

plt.xlabel("Time (s)")
plt.ylabel("State")
plt.legend()
plt.grid()
plt.show()
