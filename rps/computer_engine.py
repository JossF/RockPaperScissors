import numpy as np
from rps.schemas import num_keys


def random_choice():
    choice = np.random.randint(1, 4)
    print(num_keys[choice])
    return num_keys[choice]
