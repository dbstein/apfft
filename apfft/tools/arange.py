import numpy as np
import mpmath as mp

def arange(*args):
    """Returns a numpy array with n repetitions of mp.mpf(0)"""
    return np.array(mp.arange(*args))
