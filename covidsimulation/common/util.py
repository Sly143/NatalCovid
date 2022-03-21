from numba import jit
import numpy as np

@jit(nopython=True)
def chooseContactsNoReplace(a, size):
    return np.random.choice(a, size, replace=False)
