#source ~/miniforge3/bin/activate

import gym
#env = gym.make('CartPole-v0')
from cartpolebase import CartPoleEnv
env = CartPoleEnv()
for i_episode in range(50):
    observation = env.reset()
    for t in range(1000):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()