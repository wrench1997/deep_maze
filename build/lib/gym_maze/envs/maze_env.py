import gymnasium as gym
from cair_maze.maze_game import MazeGame


class MazeEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    id = "maze-v0"

    def __init__(self, width, height, mechanic, mechanic_args):

        self.env = MazeGame((width, height), mechanic=mechanic, mechanic_args=mechanic_args)

        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(640,480,3)) #self.env.get_state().shape
        self.action_space = gym.spaces.Discrete(4)
            
    def step(self, action):
        return self.env.step(action)

    def reset(self,seed=None):
        return self.env.reset(seed=seed)

    def render(self, mode='human',close=False):
        #mode=0
        if close:
            self.env.quit()
            return None
        return self.env.render(mode)
