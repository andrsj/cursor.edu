import matplotlib.pyplot as plt
from math import sin, pi
from numpy import array, arange, abs as np_abs
from numpy.fft import rfft, rfftfreq
import numpy as np

fd = 88200

with open("../A1laba/tens2.txt", "r") as f1:
    g0 = f1.read().splitlines()
with open("../A1laba/tens1.txt", "r") as f2:
    g1 = f2.read().splitlines()

garmoniks0 = []
garmoniks1 = []

N1 = len(g0)
N2 = len(g1)

for i in range(N1):
	garmoniks0.append(int(g0[i]))

for i in range(N2):
	garmoniks1.append(int(g1[i]))

x, y = [[i/fd for i in range(N1)],[i/fd for i in range(N2)]], [[np.hamming(N1)[i] for i in range(N1)],[np.hamming(N2)[i] for i in range(N2)]]
hmg0, hmg1 = [garmoniks0[t]*y[0][t] for t in range(N1)], [garmoniks1[t]*y[1][t] for t in range(N2)]
spectrum0, spectrum1 = rfft(garmoniks0), rfft(garmoniks1)

plt.figure()
plt.subplot(221)
plt.plot(x[0], hmg0)
plt.xlabel('T')
plt.ylabel('F1(T)')
plt.title('Одна гармоніка')
plt.grid()
plt.subplot(222)
plt.plot(x[1], hmg1)
plt.xlabel('T')
plt.ylabel('F2(T)')
plt.title('Три гармоніки')
plt.grid()
plt.subplot(223)
plt.plot(rfftfreq(N1, 1/fd), np_abs(spectrum0)/N1)
plt.xlabel('Frq')
plt.ylabel('F1(T)')
plt.title('Одна гармоніка (спектр)')
plt.grid()
plt.subplot(224)
plt.plot(rfftfreq(N2, 1/fd), np_abs(spectrum1)/N2)
plt.xlabel('Frq')
plt.ylabel('F2(T)')
plt.title('Три гармоніки (спектр)')
plt.grid()
plt.show()
