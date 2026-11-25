# P Control & PI Control

## 1. 핵심 개념

- Error: 목표값과 실제 성능의 차이
- P Control: Kp를 고려하는 제어
- Proportional Gain (Kp): 해당 시점에서의 error
- Steady-State Error: 시스템이 충분히 안정된 이후에도 남아 있는 목표값과 실제 출력값의 차이
- I Control: Integral Gain을 고려하는 제어
- Integral Gain (Ki): 누적 error
- Overshoot: 성능이 목표값이 넘어서는 현상

## 2. 핵심 수식

- P 제어: Error 값만큼을 오차 계산에 반영하는 제어
- PI 제어: P 제어에 추가적으로, 누적값인 적분 Integral을 추가로 고려한 제어. 예를 들어 P error는 계속 1이지만, 누적 I는 1, 2, 3, 4, 5, ... 이렇게 진행될 수 있음.

## 4. 핵심 질문

### P 제어만으로 오차가 남는 이유는?
P 제어는 오차가 0이 되는 순간, 제어 입력도 0으로 만듦. 따라서 꾸준히 제어 입력을 하지 않음.
### I 제어가 정상상태 오차를 줄이는 원리는?
누적 오차를 반영함
### 제어 이득을 무조건 크게 하면 안 되는 이유는?
오버슈팅이 발생할 수 있음