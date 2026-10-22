
# Week 2 — Q-learning 학습 노트

- 날짜: 2026-10-22 (목)
- 주제: Q-table, epsilon-greedy, FrozenLake
- 실습 파일: `tabular_q_learning.py`

## 1. FrozenLake 환경 이해

| 개념 | 나의 설명 | FrozenLake 예시 |
| --- | --- | --- |
| State |1~16까지 4*4 형식의 표 |구멍이 있거나 길이 있음 |
| Action |state에서 어디로 갈지 행동 |0은 왼쪽, 1은 아래, 2는 오른쪽, 3은 위 |
| Reward |행동에 대한 보상 |도착(1)하기 전까지는 모두 0 |
| Transition |action의 결과로 바뀐 next state  |state가 next_state로 바뀌는 것|
| Episode |terminated, truncated되기 전까지의 실행 횟수 |구멍에 빠지거나, 제한시간이 끝나거나, 도착하기 전까지의 횟수 |

### 생각해 볼 질문

**Q1. FrozenLake의 State 개수가 16개인 이유는?**

답: 16칸이 있으므로 16개

**Q2. CartPole과 FrozenLake의 상태 표현은 어떻게 다른가?**

답: CartPole은 state가 막대와 카트의 위치, 속도 등이었지만, FrozenLake는 1~16까지의 정수

**Q3. is_slippery=False의 의미는?**

답: 무작위로 시작하지 않도록 함

## 2. epsilon-greedy 정책

### Exploration과 Exploitation의 차이

- Exploration: 새로운 action을 탐험
- Exploitation: 최선의 reward가 보장된 action을 선택

### epsilon의 역할

- ε = 0: 탐험 0% 활용 100%
- ε = 0.2: 탐험 20% 활용 80%
- ε = 1: 탐험 100% 활용 0%

### 생각해 볼 질문

**왜 항상 Q-value가 높은 행동만 선택하면 안 되는가?**

답: 더 최선의 행동이 있음에도 불구하고, 탐험을 하지 않아 action이 고착화되므로 안됨

## 3. Q-learning 업데이트

### 업데이트 식

$$
Q(s,a) \leftarrow Q(s,a) + \alpha
[r + \gamma \max_{a'} Q(s',a') - Q(s,a)]
$$


### 실제 코드

```python
# Q-learning 업데이트 부분 직접 작성
q_value[state, action] += alpha * (reward + gamma * np.max(q_value[next_state]) - q_value[state, action])

```

## 4. FrozenLake 학습 실험

### 에피소드 수별 실험 결과

| Episodes | 최근 100회 평균 보상 | 평가 성공률 |
| --- | --- | --- |
| 100 |0.04 |100.0% |
| 1000 |0.55 |100.0% |
| 3000 |0.97 |100.0% |
