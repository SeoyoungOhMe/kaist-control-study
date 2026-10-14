
from pathlib import Path

import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

OUTPUT_DIR = Path(__file__).resolve().parent

def run_episode(env, weight, seed):
    state, info = env.reset(seed=seed)
    total_reward = 0

    while True:
        angle = state[2]
        angular_velocity = state[3]

        score = angle + weight * angular_velocity
        action = 1 if score > 0 else 0

        state, reward, terminated, truncated, info = env.step(action)
        total_reward += reward

        if terminated or truncated:
            return total_reward

weights = [0.0, 0.1, 0.3, 0.5, 1.0, 2.0]
results = {}

env = gym.make("CartPole-v1")

for weight in weights:
    rewards = []

    for episode in range(30):
        reward = run_episode(env, weight, seed=42 + episode)
        rewards.append(reward)

    results[weight] = rewards

    print(
        f"Weight={weight:.1f} | "
        f"Mean={np.mean(rewards):.2f} | "
        f"Std={np.std(rewards):.2f}"
    )

env.close()

means = [np.mean(results[w]) for w in weights]
stds = [np.std(results[w]) for w in weights]

plt.figure(figsize=(9, 5))
plt.errorbar(weights, means, yerr=stds, fmt="o-", capsize=4)
plt.xlabel("Angular velocity weight")
plt.ylabel("Mean episode reward")
plt.title("CartPole: Effect of Angular Velocity Weight")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "weight_comparison.png", dpi=150)
plt.show()
