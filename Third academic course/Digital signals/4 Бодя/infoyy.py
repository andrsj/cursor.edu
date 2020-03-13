import matplotlib.pyplot as plt
from math import sin, pi
from numpy import array, arange, abs as np_abs
from numpy.fft import rfft, rfftfreq
import numpy as np
import math

fd = 44100
v = 100000
text = "уу.txt"
with open(text, "r") as f1:
    content1 = f1.read().splitlines()

N1 = len(content1)

sound1 = []

for i in range(N1):
	sound1.append(int(v*float(content1[i])))

x = [
    [i/fd for i in range(N1)],
    # [i/fd for i in range(N2)],
    # [i/fd for i in range(N3)],
    # [i/fd for i in range(N4)],
    # [i/fd for i in range(N5)],
    # [i/fd for i in range(N6)]

]
y = [
    [np.hamming(N1)[i] for i in range(N1)],
    # [np.hamming(N2)[i] for i in range(N2)],
    # [np.hamming(N3)[i] for i in range(N3)],
    # [np.hamming(N4)[i] for i in range(N4)],
    # [np.hamming(N5)[i] for i in range(N5)],
    # [np.hamming(N6)[i] for i in range(N6)]
]

hmsound1 = []

for i in range(N1):
	hmsound1.append(sound1[i]*y[0][i])

spectrum1 = rfft(hmsound1)

n = 8
kray1 = 5600
nk = int(kray1/n)
frequncy = [[],[],[],[],[],[]]
amplitude = [[],[],[],[],[],[]]

ss = 0
n0 = 0
n1 = 0
for j in range(n):
	n1 += nk
	for i in range(n0,n1):
		ss += (np_abs(spectrum1)/N1)[i]
	amplitude[0].append(math.floor(ss))
	ss = 0
	frequncy[0].append(n1)
	n0 += nk

plt.figure()

plt.subplot(131)
plt.title(text)
plt.grid()
plt.plot(x[0], hmsound1)
plt.xlabel('T')

plt.subplot(132)
plt.title('Спектр')
plt.grid()
plt.plot(rfftfreq(N1, 1/fd), np_abs(spectrum1)/N1)

plt.subplot(133)
plt.title('Гістограма')
plt.grid()
plt.bar(range(1,n+1),amplitude[0])

plt.show()