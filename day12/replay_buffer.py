
import random
from collections import deque
import copy
import torch
import torch.nn as nn

class ReplayBuffer:
    def __init__(self, capacity=10000):
        self.buffer = deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, terminated):
        self.buffer.append(
            (state, action, reward, next_state, terminated)
        )

    def sample(self, batch_size):
        return random.sample(self.buffer, batch_size)

    def __len__(self):
        return len(self.buffer)

buffer = ReplayBuffer(capacity=100)

for i in range(10):
    buffer.push(i, 1, 1.0, i + 1, False)

print("Buffer size:", len(buffer))
print("Samples:", buffer.sample(3))


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

q_network = QNetwork()
target_network = copy.deepcopy(q_network)

target_network.eval()

target_network.load_state_dict(
    q_network.state_dict()
)