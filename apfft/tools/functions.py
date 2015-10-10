import numpy as np
import mpmath as mp

sin = np.vectorize(mp.sin)
cos = np.vectorize(mp.cos)
tan = np.vectorize(mp.tan)
exp = np.vectorize(mp.exp)
sqrt = np.vectorize(mp.sqrt)
real = np.vectorize(mp.re)
imag = np.vectorize(mp.im)
