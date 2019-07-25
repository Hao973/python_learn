# -*- coding: utf-8 -*- 
# @Time : 2019/7/19 上午11:52 
# @Author : FengHao 
# @Site :  
# @File : python_6_44_code.py
# @Software: PyCharm

import pickle
import copyreg


class GameState(object):
    def __init__(self, level=0, lives=4, points=0, magic=5):
        self.level = level
        self.lives = lives
        self.points = points
        self.magic = magic


def unpickle_game_state(kwargs):
    return GameState(**kwargs)


def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    return unpickle_game_state, (kwargs,)


copyreg.pickle(GameState, pickle_game_state)


def test_1():
    state = GameState()
    state.level += 1  # Player beat a level
    state.lives -= 1  # Player had to try again
    state_path = './tmp/game_state.bin'
    with open(state_path, 'wb') as f:
        pickle.dump(state, f)

    with open(state_path, 'rb') as f:
        state_after = pickle.load(f)

    print(state_after.__dict__)


def test_2():
    # state = GameState()
    # serialized = pickle.dumps(state)
    # state_after = pickle.loads(serialized)
    # print(state_after.__dict__)
    state_path = './tmp/game_state.bin'
    with open(state_path, 'rb') as f:
        state_after = pickle.load(f)

    print(state_after.__dict__)


def test_3():
    state = GameState()
    state.points += 1000
    serialized = pickle.dumps(state)
    state_after = pickle.loads(serialized)
    print(state_after.__dict__)


if __name__ == '__main__':
    g_serialized = None
    # test_1()
    test_2()
    test_3()
