import gym
from tqdm import tqdm

env = gym.make('CartPole-v0')
env = gym.wrappers.Monitor(env, "record_dir", force=True)
for i in tqdm(range(2)):
    obs, done, rew = env.reset(), False, 0
    while (done != True) :
        A =  agent.get_action(obs, env.action_space.n, epsilon = 0)
        obs, reward, done, info = env.step(A.item())
        rew += reward
        sleep(0.01)
        env.render()  
    print("episode : {}, reward : {}".format(i,rew)) 