# Week 5 · 수요일 학습 노트 (2026-11-11)

**주제:** Euler 적분 구현과 시간 간격(Δt) 비교  

## 2. 핵심 개념 (내 말로 작성)

**상태 변수** `s = [x, v]`가 의미하는 것은?

> 상태를 위치와 속도로 표현한다는 뜻

**운동 방정식** (질량 m, 감쇠 계수 c, 스프링 상수 k)

- `dx/dt = v`
- `dv/dt = a`

**Euler 업데이트 식**

- `x_next = x + v * dt`
- `v_next = v + a * dt`

왜 현재 상태를 이용해 다음 상태를 계산할 수 있을까?

> 현재의 x, v를 알면, 질량-스프링-댐퍼 식에 의해 a를 계산할 수 있고, 오일러 방법에 의해 다음 x, v 값을 알 수 있음

## 4. 직접 구현

파일명 예시: `euler_simulation.py`

```python
import numpy as np
import matplotlib.pyplot as plt

m, k, c = 1.0, 4.0, 0.4
x0, v0 = 1.0, 0.0
T = 10.0

def simulate_euler(dt):
    n_steps = round(T / dt)
    t = np.linspace(0, T, n_steps + 1)
    x = np.zeros(n_steps + 1)
    v = np.zeros(n_steps + 1)
    x[0], v[0] = x0, v0

    for i in range(n_steps):
        a = (-k * x[i] - c * v[i]) / m
        x[i + 1] = x[i] + dt * v[i]
        v[i + 1] = v[i] + dt * a

    return t, x, v

for dt in [0.2, 0.05, 0.01]:
    t, x, v = simulate_euler(dt)
    plt.plot(t, x, label=f'dt={dt}s')

plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Euler integration: effect of time step')
plt.grid(True)
plt.legend()
plt.show()
```

## 6. 스스로 설명하기

1. Euler 방법의 핵심 아이디어를 한 문장으로 설명하면?
   > 현재의 위치와 속도를 알면, 일정 시간 이후의 위치와 속도도 알 수 있음
2. 왜 `x[i + 1] = x[i] + v[i] * dt`인가?
   > v = dx/dt -> dx = v * dt -> x_next = x + v * dt
3. Δt가 크면 반복 횟수가 적어지는데, 단점은 무엇인가?
   > 그만큼 정확도와 변화에 대한 대응이 떨어짐
4. Δt가 작은데도 결과가 완벽하게 정확한 것은 아닌 이유는?
   > 오일러 방식은 현재의 상태가 미래에도 동일함을 가정하므로, 미래의 유동적인 변화를 고려하지 않음
5. 오늘 실습을 로봇이나 드론 시뮬레이션과 연결하면?
   > 로봇이나 드론 시뮬레이션도 현재의 상태를 알면 미래의 상태를 예측할 수 있음
