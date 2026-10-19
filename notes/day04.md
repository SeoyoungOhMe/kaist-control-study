# Week 2 · Day 1 — 셀프 설명 노트

**날짜:** 2026-10-19 (월)  
**주제:** 상태·행동·보상·전이, Return, V-value와 Q-value

## 5단계. 오늘 배운 내용 설명하고 마무리
### 1. State, Action, Reward, Transition을 각각 설명할 수 있는가?

**내 답변:**

- **State:** Agent의 상태로, 위치나 속도, 각속도 등에 해당
- **Action:** 0 또는 1 값으로 왼쪽이나 오른쪽으로 이동하는 정보
- **Reward:** 어떤 action에 대한 보상으로, 클수록 좋음
- **Transition:** state를 바꾸는 행위

### 2. 즉시 보상이 0인데도 좋은 행동일 수 있는 이유는?

**내 답변:** 미래의 잠재적 보상이 더 클 수 있기 때문


### 3. Return과 즉시 Reward의 차이는?

**내 답변:** Return은 누적 보상으로 미래의 보상이 모두 합쳐진 값, 즉시 Reward는 Action 1회 시 발생하는 보상


### 4. V(s)와 Q(s, a)의 차이는?

**내 답변:** V(s)는 state에 대한 보상이고, Q(s, a)는 action에 대한 state에서의 보상


### 5. Q-table에서 가장 좋은 행동을 어떻게 찾는가?

**내 답변:** best action에 대하여 더 높은 확률을 부여하면 됨.


---
