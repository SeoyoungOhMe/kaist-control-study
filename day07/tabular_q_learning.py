
import gymnasium as gym
import numpy as np

env = gym.make(
    "FrozenLake-v1",
    map_name="4x4",
    is_slippery=False
)

print("State 개수:", env.observation_space.n)
print("Action 개수:", env.action_space.n)

state, info = env.reset()
print("초기 상태:", state)

n_states = env.observation_space.n
n_actions = env.action_space.n

q_table = np.zeros((n_states, n_actions))

print("Q-table shape:", q_table.shape)
print(q_table)

q_table[0, 1] = 0.8
q_table[0, 2] = 0.3

print(q_table[0])
print(np.argmax(q_table[0]))
print(np.max(q_table[0]))

def epsilon_greedy(q_table, state, epsilon, rng):
    if rng.random() < epsilon:
        # Exploration
        action = int(rng.integers(q_table.shape[1]))
    else:
        # Exploitation
        action = int(np.argmax(q_table[state]))

    return action

def train_q_learning(
    env,
    episodes,
    alpha=0.1,
    gamma=0.99
):
    n_states = env.observation_space.n
    n_actions = env.action_space.n

    q_table = np.zeros((n_states, n_actions))

    # Hyperparameters
    epsilon = 1.0
    epsilon_min = 0.05
    epsilon_decay = 0.999

    rng = np.random.default_rng(42)
    rewards = []

    for episode in range(episodes):
        state, _ = env.reset(seed=42 + episode)
        done = False
        total_reward = 0

        while not done:

            # 1. 행동 선택
            action = epsilon_greedy(
                q_table, state, epsilon, rng
            )

            # 2. 환경에서 행동 실행
            next_state, reward, terminated, truncated, _ = (
                env.step(action)
            )

            # 3. TD target 계산
            if terminated:
                td_target = reward
            else :
                td_target = reward + gamma * np.max(q_table[next_state])

            # 4. Q-table 업데이트
            q_table[state, action] += alpha * (td_target - q_table[state, action])

            # 5. 다음 상태로 이동
            state = next_state
            total_reward += reward
            done = terminated or truncated

        rewards.append(total_reward)

        # 6. 탐험 확률 감소
        epsilon = max(
            epsilon_min,
            epsilon * epsilon_decay
        )

    return q_table, np.array(rewards)

def evaluate(env, q_table, episodes=100):
    successes = 0

    for episode in range(episodes):
        state, _ = env.reset(seed=10000 + episode)
        done = False

        while not done:
            action = int(np.argmax(q_table[state]))

            state, reward, terminated, truncated, _ = (
                env.step(action)
            )

            successes += reward
            done = terminated or truncated

    return successes / episodes

experiments = {
    "baseline": (0.1, 0.99),
    "high_alpha": (0.5, 0.99),
    "zero_gamma": (0.1, 0.0),
}

results = {}

for name, (alpha, gamma) in experiments.items():
    q_table, rewards = train_q_learning(
        env,
        episodes=3000,
        alpha=alpha,
        gamma=gamma
    )

    success_rate = evaluate(env, q_table)

    results[name] = rewards

    print(
        f"{name}: "
        f"recent_reward={np.mean(rewards[-100:]):.3f}, "
        f"eval_success={success_rate:.1%}"
    )

env.close()


import matplotlib.pyplot as plt

window = 100

for name, rewards in results.items():
    moving_avg = np.convolve(
        rewards,
        np.ones(window) / window,
        mode="valid"
    )

    plt.plot(
        np.arange(window, len(rewards) + 1),
        moving_avg,
        label=name
    )

plt.xlabel("Episode")
plt.ylabel("Average Reward (100 Episodes)")
plt.title("Q-learning Training Progress")
plt.legend()
plt.grid(True)
plt.savefig("q_learning_results.png")
plt.show()
