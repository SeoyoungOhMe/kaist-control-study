
import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt


# Policy A: Random
def random_policy(state, env):
    return env.action_space.sample()


# Policy B: Angle
def angle_policy(state, env):
    angle = state[2]
    return 1 if angle > 0 else 0


# Policy C: Angle + Angular Velocity
def angle_velocity_policy(state, env):
    angle = state[2]
    angular_velocity = state[3]

    return 1 if angle + 0.5 * angular_velocity > 0 else 0

def linear_policy(state, env):
    weights = np.array([0, 0, 1, 2.0])

    score = np.dot(weights, state)

    return 1 if score > 0 else 0

def run_episode(env, policy, seed):
    state, info = env.reset(seed=seed)
    env.action_space.seed(seed)

    total_reward = 0

    while True :
        action = policy(state, env)

        next_state, reward, terminated, truncated, info = env.step(action)

        total_reward += reward
        state = next_state

        if terminated or truncated :
            return total_reward

policies = {
    "Random": random_policy,
    "Angle": angle_policy,
    "Angle + Velocity": angle_velocity_policy,
    "Linear": linear_policy,
}

results = {}

for policy_name, policy_fn in policies.items():
    env = gym.make("CartPole-v1")
    rewards = []

    for episode in range(30):
        reward = run_episode(
            env,
            policy_fn,
            seed=42 + episode
        )
        rewards.append(reward)

    env.close()
    results[policy_name] = rewards

    print(f"\nPolicy: {policy_name}")
    print(f"Mean reward: {np.mean(rewards):.2f}")
    print(f"Std reward: {np.std(rewards):.2f}")
    print(f"Min reward: {np.min(rewards):.0f}")
    print(f"Max reward: {np.max(rewards):.0f}")

# 1. 에피소드별 Reward
plt.figure(figsize=(10, 5))

for name, rewards in results.items():
    plt.plot(
        range(1, len(rewards) + 1),
        rewards,
        label=name,
        alpha=0.8
    )

plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.title("CartPole Policy Comparison")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("day02/reward_comparison.png")
plt.show()
