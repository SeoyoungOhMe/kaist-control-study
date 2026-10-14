
from pathlib import Path

import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

OUTPUT_DIR = Path(__file__).resolve().parent


# 1. 상태 벡터와 가중치 벡터의 내적으로 행동 결정
def linear_policy(state, weights):
    score = np.dot(weights, state)
    return 1 if score > 0 else 0


# 2. 하나의 에피소드 실행
def run_episode(env, weights, seed):
    state, info = env.reset(seed=seed)
    total_reward = 0

    while True:
        action = linear_policy(state, weights)

        state, reward, terminated, truncated, info = env.step(action)
        total_reward += reward

        if terminated or truncated:
            return total_reward


# 3. 비교할 두 가지 가중치 벡터
policies = {
    "Original": np.array([0, 0, 1, 0.5]),
    "Full State": np.array([0.05, 0.1, 1, 0.5])
}

results = {}

env = gym.make("CartPole-v1")

# 4. 정책별 30개 에피소드 실행
for policy_name, weights in policies.items():
    rewards = []

    for episode in range(30):
        reward = run_episode(
            env,
            weights,
            seed=42 + episode
        )
        rewards.append(reward)

    results[policy_name] = rewards

    print(f"\nPolicy: {policy_name}")
    print(f"Mean Reward: {np.mean(rewards):.2f}")
    print(f"Std Reward: {np.std(rewards):.2f}")

env.close()


# 5. 평균 보상과 표준편차 비교
names = list(results.keys())
means = [np.mean(results[name]) for name in names]
stds = [np.std(results[name]) for name in names]

plt.figure(figsize=(8, 5))
plt.bar(names, means, yerr=stds, capsize=5)

plt.xlabel("Policy")
plt.ylabel("Mean Episode Reward")
plt.title("CartPole: Original vs Full-State Policy")
plt.ylim(0, 550)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "full_state_comparison.png", dpi=150)
plt.show()
