
import torch
import torch.nn as nn

import random

def select_action(state, epsilon=0.2):
    if random.random() < epsilon:
        return random.choice([0, 1])

    with torch.no_grad():
        state_tensor = torch.tensor(
            state, dtype=torch.float32
        )
        q_values = q_network(state_tensor)

    return torch.argmax(q_values).item()

class QNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(4, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 2)
        )

    def forward(self, state):
        return self.net(state)


from collections import deque

class ReplayBuffer:
    def __init__(self, capacity=10000):
        self.buffer = deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        self.buffer.append(
            (state, action, reward, next_state, done)
        )

    def sample(self, batch_size):
        return random.sample(self.buffer, batch_size)

    def __len__(self):
        return len(self.buffer)

buffer = ReplayBuffer()

for i in range(10):
    buffer.push(
        state=[i, 0, 0, 0],
        action=i % 2,
        reward=1.0,
        next_state=[i + 1, 0, 0, 0],
        done=False
    )

print("Buffer size:", len(buffer))

batch = buffer.sample(4)

for experience in batch:
    print(experience)


q_network = QNetwork()

state = torch.tensor(
    [0.1, 0.2, -0.1, 0.3],
    dtype=torch.float32 
)

with torch.no_grad():
    q_values = q_network(state)

print("Q-values:", q_values)
print("Shape:", q_values.shape)

action = torch.argmax(q_values).item()
print("Selected action:", action)

# 동작 확인
for i in range(10):
    action = select_action([0.1, 0.2, -0.1, 0.3])
    print(f"{i}: action={action}")