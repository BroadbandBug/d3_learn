
import numpy as np
from numpy.fft import fft, fftfreq

t = np.linspace(0, 10, 512)
freq = 1
sig = np.sin(t * freq * 2 * 3.141)

sp = fft(sig)
freq = fftfreq(sig.size, d=0.001)

print "index, freq"
for ii, result in enumerate( np.abs(freq) ):
    print "%i,%f" % (ii, result)

