import numpy as np
from rps.schemas import num_keys, get_winner
from rps.blackboard import Blackboard


class Computer:

    def __init__(self, blackboard_inst: Blackboard):
        super(Computer, self).__init__()
        self.bb = blackboard_inst

    def make_choice(self):
        expected_move = self.random_choice
        if self.bb.move_averages(from_last=5).idxmax():
            expected_move = self.bb.move_averages(from_last=5).idxmax()
        return get_winner[expected_move]

    @staticmethod
    def random_choice():
        choice = np.random.randint(1, 4)
        print(num_keys[choice])
        return num_keys[choice]
