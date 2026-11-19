
import numpy as np

# 1. 시스템 파라미터
m = 1.0
c = 2.0
k = 3.0

# 2. 상태공간 행렬
A = np.array([
    [0, 1],
    [-k/m, -c/m]
])

B = np.array([
    [0],
    [1/m]
])

C = np.array([[1, 0]])
D = np.array([[0]])

# 3. 현재 상태: 위치 1m, 속도 0m/s
x = np.array([
    [1.0],
    [0.0]
])

# 4. 외부 힘 1N
u = np.array([[1.0]])

# 5. 상태 변화율과 출력 계산
x_dot = A @ x + B @ u
y = C @ x + D @ u

print("A:\n", A)
print("B:\n", B)
print("상태 변화율:\n", x_dot)
print("출력:\n", y)
