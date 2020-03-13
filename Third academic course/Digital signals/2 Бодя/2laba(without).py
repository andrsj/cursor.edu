import matplotlib.pyplot as plt
from math import sin, pi
from numpy import array, arange, abs as np_abs
from numpy.fft import rfft, rfftfreq
import numpy as np

f2 = 10**2
f1 = f2/2
f0 = f2/4
fd = (f2*2)*5
N = 10**2
vl = 10**2

garmoniks0, garmoniks1 = [vl*sin(2*pi*f0*t/fd) for t in range(N)], [vl*(sin(2*pi*f0*t/fd) + 20*sin(2*pi*f1*t/fd) + 3*sin(2*pi*f2*t/fd)) for t in range(N)]
spectrum0, spectrum1 = rfft(garmoniks0), rfft(garmoniks1)
x = [i/fd for i in range(N)]

plt.figure()
plt.subplot(221)
plt.plot(x, garmoniks0)
plt.xlabel('T')
plt.ylabel('F1(T)')
plt.title('Одна гармоніка')
plt.subplot(222)
plt.plot(x, garmoniks1)
plt.xlabel('T')
plt.ylabel('F2(T)')
plt.title('Три гармоніки')
plt.subplot(223)
plt.plot(rfftfreq(N, 1/fd), np_abs(spectrum0)/N)
plt.xlabel('Frq')
plt.ylabel('F1(T)')
plt.title('Одна гармоніка (спектр)')
plt.subplot(224)
plt.plot(rfftfreq(N, 1/fd), np_abs(spectrum1)/N)
plt.xlabel('Frq')
plt.ylabel('F2(T)')
plt.title('Три гармоніки (спектр)')
plt.grid()
plt.show()
