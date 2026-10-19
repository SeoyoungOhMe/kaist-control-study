
import gymnasium as gym

env = gym.make("FrozenLake-v1", is_slippery=False)

state, info = env.reset(seed=42)
action = 2  # 오른쪽

next_state, reward, terminated, truncated, info = env.step(action)

print("State:", state)
print("Action:", action)
print("Next State:", next_state)
print("Reward:", reward)
print("Terminated:", terminated)

env.close()
