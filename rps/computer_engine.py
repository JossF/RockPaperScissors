import numpy as np
from rps.schemas import num_keys


def random_choice():
    return num_keys[np.random.randint(1,3)]
