import matplotlib.pyplot as plt
from math import sin, pi
from numpy import array, arange, abs as np_abs
from numpy.fft import rfft, rfftfreq
import numpy as np

fd = 88200 * 2

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

x = [[i/fd for i in range(N1)],[i/fd for i in range(N2)]]
spectrum0, spectrum1 = rfft(garmoniks0), rfft(garmoniks1)

plt.figure()
plt.subplot(221)
plt.plot(x[0], garmoniks0)
plt.xlabel('T')
plt.ylabel('F1(T)')
plt.title('Одна гармоніка')
plt.grid()
plt.subplot(222)
plt.plot(x[1], garmoniks1)
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