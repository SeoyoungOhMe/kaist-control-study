
import numpy as np
import matplotlib.pyplot as plt

# 1. 물리 파라미터
m = 1.0
k = 4.0
c = 0.5

# 2. 초기 상태
x = 1.0
v = 0.0

# 3. 시간 설정
dt = 0.01
T = 10.0
steps = int(T / dt)

positions = []
velocities = []
times = []

# 4. 시뮬레이션
for i in range(steps + 1):
    t = i * dt

    times.append(t)
    positions.append(x)
    velocities.append(v)

    # TODO 1: 가속도 계산
    a = (-k * x - c * v) / m

    # 마지막 시점에는 갱신할 필요 없음
    if i == steps:
        break

    # TODO 2: 다음 위치 계산
    next_x = x + v * dt

    # TODO 3: 다음 속도 계산
    next_v = v + a * dt

    x = next_x
    v = next_v

# 5. 결과 시각화
plt.plot(times, positions, label="Position")
plt.plot(times, velocities, label="Velocity")
plt.xlabel("Time (s)")
plt.ylabel("State value")
plt.legend()
plt.grid()
plt.show()
