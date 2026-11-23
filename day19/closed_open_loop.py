import numpy as np
import matplotlib.pyplot as plt

dt = 0.1
T = 15
t = np.arange(0, T + dt, dt)

target = 10
Kp = 0.5 # k는 비례이득(Proportional Gain)

h_open = np.zeros(len(t)) # 개루프
h_closed = np.zeros(len(t)) # 폐루프

for i in range(len(t) - 1):
    # 개루프: 현재 고도를 보지 않고 일정한 명령 사용
    u_open = 1.0 if t[i] < 10 else 0.0
    h_open[i + 1] = h_open[i] + u_open * dt

    # 폐루프: 현재 고도를 측정하여 오차 계산
    error = target - h_closed[i]
    u_closed = Kp * error

    h_closed[i + 1] = h_closed[i] + u_closed * dt

plt.plot(t, h_open, label="Open-loop")
plt.plot(t, h_closed, label="Closed-loop")
plt.axhline(target, color="black",
            linestyle="--", label="Target")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.legend()
plt.grid()
plt.show()