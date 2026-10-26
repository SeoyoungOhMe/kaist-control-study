
# Week 2 — Q-learning 학습 정리

- 날짜: 2026-10-25
- 주제: Q-learning 실험 및 DQN 준비

## 1. Q-learning 핵심 개념

### Q-learning 업데이트 식

$$
Q(s,a) \leftarrow Q(s,a) + \alpha[r + \gamma \max_{a'}Q(s',a') - Q(s,a)]
$$

- Q(s,a): Quality Function(가치 함수). 특정 action을 했을 때의 미래 가치
- α (학습률): 학습을 통해 갱신하고자 하는 예상값과 타겟값의 차이를 얼마나 반영할지에 대한 비율. 학습률이 높을수록 학습된 값을 많이 반영하게 됨.
- γ (할인율): 미래 가치에 대해 얼마나 반영할지에 대한 비율. 미래값은 현재값과 달리 확실하지 않으므로 0부터 1 사이의 값을 곱해서 반영함
- r (보상): 
- TD Target: reward + gamma * np.max(q_table[next_state]). 현재의 보상값과 미래에 최대로 받을 보상을 더한 값
- TD Error: TD Target으로 계산한 보상값과 예상값의 차이

## 2. 하이퍼파라미터 실험

| 실험 | Alpha | Gamma | 평균 보상 | 성공률 |
| --- | --- | --- | --- | --- |
| Baseline | 0.1 | 0.99 |0.970 |100% |
| High Alpha | 0.5 | 0.99 |0.960 |100% |
| Zero Gamma | 0.1 | 0.0 |0.0 |0% |

### 평균 보상 그래프

![Q-learning 학습 결과](/day07/q_learning_results.png)

- 그래프에서 관찰한 점: high_alpha와 baseline은 episode마다 우위가 바뀌기도 함

## 3. CartPole과 Q-learning

### FrozenLake와 CartPole의 차이

- FrozenLake 상태 공간:
- CartPole 상태 공간:

### CartPole에서 Q-table을 사용하기 어려운 이유

- CartPole은 state가 4가지 백터값으로 표현되는데, 이걸 매번 저장하면 너무 큼

### 신경망으로 Q-table을 대체하면?

- DQN을 통해 신경망에 Q-value 계산값을 주입

### 느낀 점

- 행동의 가치를 수학적으로 함수로 표현할 수 있다는 사실이 매우 흥미로웠다.
- DQN에 대해 더 깊이 이해하고 싶다.

