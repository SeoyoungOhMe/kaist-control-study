
import gymnasium as gym
import numpy as np

# 1. 환경 생성
env = gym.make("CartPole-v1", render_mode="human")

episode_rewards = []
# 2. 에피소드 5번 실행
for episode in range(5):
    state, info = env.reset(seed=42 + episode)
    total_reward = 0
    step_count = 0

    while True:
        # 3. 무작위 행동 선택
        action = env.action_space.sample()
        # action = 1

        # 4. 환경에 행동 전달
        next_state, reward, terminated, truncated, info = env.step(action)  # 행동 한 단계 실행

        if step_count < 3:
            print(
                f"Episode {episode+1}, step {step_count}: "
                f"state={np.round(state, 3)}, "
                f"action={action}, reward={reward}"
            )

        total_reward += reward
        step_count += 1
        state = next_state 

        # 5. 에피소드 종료 확인
        if terminated or truncated:
            break

    episode_rewards.append(total_reward)
    print(f"Episode {episode+1}: Reward = {total_reward}")

env.close()

print(f"Average reward: {np.mean(episode_rewards):.2f}")
