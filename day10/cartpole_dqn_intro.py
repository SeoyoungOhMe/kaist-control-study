
import gymnasium as gym

env = gym.make("CartPole-v1")

print("Observation space:", env.observation_space)
print("Action space:", env.action_space)

state, info = env.reset(seed=42)

print("\nInitial state:", state)
print("State shape:", state.shape)

for i in range(5):
    action = env.action_space.sample()

    next_state, reward, terminated, truncated, info = env.step(action)

    print(f"\nStep {i + 1}")
    print("State:", next_state)
    print("Action:", action)
    print("Reward:", reward)

    print("Number of states:", env.observation_space.shape[0])
    print("Number of actions:", env.action_space.n)

    if terminated or truncated:
        next_state, info = env.reset()

    state = next_state

env.close()
