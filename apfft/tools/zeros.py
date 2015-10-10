import numpy as np
import mpmath as mp

def zeros(n):
    """Returns a numpy array with n repetitions of mp.mpf(0)"""
    return np.array(mp.zeros(n,1))

def czeros(n):
    """Returns a numpy array with n repetitions of mp.mpc(0)"""
    return np.array(mp.zeros(n,1)) * mp.mpc(0,0)
