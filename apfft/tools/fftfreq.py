import numpy as np
import mpmath as mp
from numpy.compat import integer_types

def fftfreq(n,d=mp.mpf(1.0)):
    """
    Return the Discrete Fourier Transform sample frequencies.
    Same as numpy.fft.fftfreq, but with precision given by mp.mp.dps
    """
    if not isinstance(n, integer_types):
        raise ValueError("n should be an integer")
    val = mp.mpf(1) / (n * d)
    results = np.empty(n, int)
    N = (n-1)//2 + 1
    p1 = np.arange(0, N, dtype=int)
    results[:N] = p1
    p2 = np.arange(-(n//2), 0, dtype=int)
    results[N:] = p2
    return results * val
