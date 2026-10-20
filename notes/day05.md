## Week 2 Day 2 — Bellman & Q-learning

### 1. Bellman 방정식
- Bellman 방정식이 필요한 이유: 미래 value를 통해 현재 action의 value를 계산할 수 있기 때문
- 현재 가치와 미래 가치의 관계: 미래 가치에 의해 현재 가치를 계산할 수 있음

### 2. Q-learning 업데이트 식
- 업데이트 공식: q(s,a) = q(s,a) + alpha * (r + gamma * q(s(t+1), a) - q(s,a))
- α(학습률)의 의미: 현재와 미래 value의 차이값을 얼마나 반영할 건지에 대한 비율
- γ(할인율)의 의미: 미래 value를 얼마나 반영할 건지에 대한 비율
- TD Target의 의미: r + gamma * q(s(t+1), a). 새로운 목표 value
- TD Error의 의미: r + gamma * q(s(t+1), a) - q(s,a). 현재와 미래 value의 차이

### 3. Python 실험
- alpha 변경 결과: alpha를 높일수록 현재와 미래 value 차이를 반영하는 비율이 높아져 new q-value값이 높아짐
- gamma 변경 결과: gamma를 높일수록 미래 value를 반영하는 비율이 높아짐. gamma가 0이면 미래 value를 반영하지 않는 마지막 값(terminated)
- 업데이트 순서를 바꾼 결과: 미래의 value를 계산하지 않아 q(s(t+1), a)가 0이므로 new q-value도 old q-value와 동일

### 4. 오늘의 셀프 설명
- 에이전트는 Q-value를 어떻게 학습하는가? 미래의 value와 현재 value 차이를 계산해 현재 value 값에 더하여 반영
- 보상이 0이어도 Q-value가 증가할 수 있는가? 맞음. 현재 보상 뿐만 아니라 미래 q-value 값도 반영하기 때문
- Bellman 방정식과 Q-learning 업데이트는 어떤 관계인가? Bellman 방정식은 미래의 value가 현재의 value 계산에 이용된다는 의미를 가짐. Q-learning은 Bellman 방정식을 일부로 이용해 미래와 현재 value 차이를 계산할 때 사용함.

### 5. 내일 복습할 내용
- 헷갈린 점: 미래 value를 꼭 끝에서부터 계산해와야한다면 비효율적인 거 아닌가?
- 다시 확인할 개념: Q-value의 python 구현
