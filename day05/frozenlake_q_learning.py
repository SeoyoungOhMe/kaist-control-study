
import numpy as np

# 16개 상태, 4개 행동
Q = np.zeros((16, 4))

alpha = 1.0
gamma = 0.3

def update_q(state, action, reward, next_state, terminated):
    old_q = Q[state, action]

    if terminated:
        next_max_q = 0.0
    else:
        next_max_q = np.max(Q[next_state])

    target = reward + gamma * next_max_q
    td_error = target - old_q

    Q[state, action] += alpha * td_error

    print(f"State: {state}, Action: {action}")
    print(f"Old Q: {old_q:.3f}")
    print(f"Target: {target:.3f}")
    print(f"TD Error: {td_error:.3f}")
    print(f"New Q: {Q[state, action]:.3f}")
    print()

# 1. 상태 14에서 오른쪽으로 이동해 목표 도착
update_q(
    state=14,
    action=2,
    reward=1,
    next_state=15,
    terminated=True
)

# 2. 상태 13에서 오른쪽으로 이동
update_q(
    state=13,
    action=2,
    reward=0,
    next_state=14,
    terminated=False
)

print("Q[13]:", Q[13])
print("Q[14]:", Q[14])
