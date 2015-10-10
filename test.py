import numpy as np
import mpmath as mp
import apfft

"""
Test program for Arbitrary Precision fft

First test:  compares FFT of sin(x) to exact FFT
Second test:  compares IFFT(FFT(sin(x))) to sin(x)
Third test:  compares IFFT(FFT(sin(x)) * 1j * fftfreq(N)) to cos(x)
"""

# set precsion to 100 digits
mp.mp.dps = 100
# set size of transform to test
N = 16

# construct 
x = mp.linspace( mp.mpf(0), mp.mpf(2.0)*mp.pi, 16, endpoint=False )
y = apfft.tools.sin( x )

# take the fft
yh = apfft.fft(y)
# check to make sure we got the correct transform
true_transform = apfft.tools.czeros(N)
true_transform[1] = -mp.mpc(0,N/2)
true_transform[-1] = mp.mpc(0,N/2)
diff = float(np.max(np.abs(yh-true_transform)))
print 'Test 1:', '{:0.2e}'.format(diff)

# now take the ifft
ya = apfft.ifft(yh)
# check vs the original solution
diff = float(np.max(np.abs(ya - y)))
print 'Test 2:', '{:0.2e}'.format(diff)

# compute cos(x)
cx = apfft.tools.cos(x)
# compute the derivative of sin(x)
k = apfft.tools.fftfreq(N,mp.mpf(1.0/N))
w1 = yh * k * mp.mpc(0,1)
w2 = apfft.tools.real(apfft.ifft(w1))
diff = float(np.max(np.abs(cx - w2)))
print 'Test 3:', '{:0.2e}'.format(diff)
