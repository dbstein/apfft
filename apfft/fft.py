import numpy as np
import mpmath as mp
import apfft

def fft(yg):
    """
    Performs an fft in arbitrary precision arithmetic
    Arithmetic is implemented via the package mpmath
    Precision should be set by setting the variable mp.mp.dps to the desired precision

    Input:
    yg: 1D numpy vector, with yg.shape[0] a power of 2
        elements of yg should be of type mp.mpc

    Currently, the input vector must have a length given by a power of 2
    The algorithm used here was based on code posted at https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/
    """
    N = yg.shape[0]
    if np.log2(N) % 1 > 0:
        raise ValueError("size of x must be a power of 2")
    N_min = min(N, 8)
    # Perform an O[N^2] DFT on all length-N_min sub-problems at once
    n = apfft.tools.arange(N_min)
    k = n[:, None]
    A = -mp.mpc(2j) * mp.pi * n * k / mp.mpf(N_min)
    M = apfft.tools.exp(A)
    X = M.dot(yg.reshape((N_min, -1)))
    while X.shape[0] < N:
        X_even = X[:, :X.shape[1] / 2]
        X_odd = X[:, X.shape[1] / 2:]
        A = -mp.mpc(1j) * mp.pi * apfft.tools.arange(X.shape[0]) / mp.mpf(X.shape[0])
        factor = apfft.tools.exp(A)[:, None]
        X = np.vstack([X_even + factor * X_odd,
                       X_even - factor * X_odd])
    # build-up each level of the recursive calculation all at once
    return X.ravel()
