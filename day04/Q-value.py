
import numpy as np

# 상태 16개, 행동 4개
Q = np.zeros((16, 4))

# 학습된 값이 아닌 임의의 예시
Q[0] = [0.1, 0.2, 0.6, 0.3]
Q[1] = [0.7, 0.1, 0.3, 0.2]

state = 1

# 가장 높은 Q-value를 가진 행동
best_action = np.argmax(Q[state])

# 해당 행동의 Q-value
best_q = np.max(Q[state])

# 모든 행동을 동일한 확률로 선택하는 정책
policy = np.ones(4) / 4
# policy = np.array([0.1, 0.1, 0.7, 0.1])

# 해당 정책을 기준으로 계산한 상태 가치 추정
state_value = np.sum(policy * Q[state])

print("Q-values:", Q[state])
print("Best action:", best_action)
print("Best Q-value:", best_q)
print("Estimated V(s):", state_value)
