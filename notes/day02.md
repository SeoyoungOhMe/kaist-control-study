# Day 02 — CartPole Policy Comparison

## 1. 실험 목표
세 가지 정책의 성능을 비교하고 상태, 행동, 보상의 관계를 이해한다.

## 2. 실험 조건
- 환경: CartPole-v1
- Episode: 정책별 30회
- 초기 Seed: 42~71
- 평가 지표: 평균 Reward, 표준편차, 최대·최소 Reward

## 3. 실험 결과

| Policy | Mean Reward | Std Reward |
|---|---|---|
| Random |25.73|17.96 |
| Angle |43.53 |8.38 |
| Angle + Angular Velocity |500.00 |0.00 |

## 4. 결과 분석
- 가장 좋은 정책: Angle + Angular Velocity
- 가장 안정적인 정책: Angle + Angular Velocity
- 예상과 달랐던 결과: Angle -> Mean Reward 작음
- 그 이유에 대한 가설: Reward를 결정할 때 단순히 막대의 각도만 고려하면 부족

## 5. 선형대수 연결
기존의 `angle + 0.5 * angular_velocity` 정책은 `np.dot(weights, state)`로 표현할 수 있다.

- 상태 벡터: np.array([x, x_dot, y, y_dot])
- 가중치 벡터: np.array([0, 0, 1, 0.5])
- 가중치를 바꾸면 달라지는 점: 규칙기반의 action 값이 달라지므로, 결과적으로 reward의 mean, std가 달라짐

## 6. 오늘 배운 개념
- Policy: 정책. 예를 들면 np.dot(state, weights). 무작위로, 막대의 각도에 따라서, 혹은 막대의 각도와 각속도의 수식 등으로 표현
- MDP: Markov Decision Policy. State에 따라 Action을 결정하는 규칙 기반 제어.
- Linear Policy: state와 weights를 내적하는 정책. np.dot(state, weights)로 표현
- Standard Deviation: 표준 편차

## 7. 다음에 알아볼 질문
1. 사람이 가중치를 직접 정하지 않고 컴퓨터가 학습하게 하려면?
2. 상태 벡터의 네 가지 값을 모두 활용하면 성능이 좋아질까?
3. Reward 뿐 아니라 성능을 나타낼 수 있는 지표가 없을까?
4. Angle + Velocity 는 어떻게 Std reword가 0.00일 수 있을까?