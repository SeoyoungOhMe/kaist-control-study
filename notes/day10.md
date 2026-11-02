
# Week 4 - Monday: DQN 기초

## 1. Q-learning vs DQN

### Q-learning
- Q-value 저장 방식: 배열 테이블에 저장
- 연속 상태 처리 시 문제점: 전부 테이블에 저장하기 어려움

### DQN
- Q-value 예측 방식: 신경망을 통해 action을 선택
- 신경망이 학습하는 것: state의 4가지 상태를 학습
- 경사하강법과의 관계: 

## 2. CartPole 환경 분석
- Observation shape: (4,1)
- Action space: (2,1)
- state[0]: 카트 위치
- state[1]: 카트 속도
- state[2]: 막대 속도
- state[3]: 막대 각속도

## 3. Q-network 설계
- 입력 뉴런 수: 4
- 은닉 뉴런 수: 32
- 출력 뉴런 수: 2
- 출력값의 의미: action 2가지 (0, 1)

## 6. 아직 이해하지 못한 것
- DQN과 경사하강법의 관계

## 7. 내일 할 일
- PyTorch로 Q-network 구현
- 상태를 입력해 Q-value 출력 확인
- epsilon-greedy 정책 연결
