from setuptools import setup

setup(name='gym_maze',
      version='2.0.1',
      install_requires=['gymnasium', 'numpy', 'pygame==2.1.2', 'scikit-image'],
      packages=['gym_maze', 'gym_maze.envs', 'cair_maze']
      )
