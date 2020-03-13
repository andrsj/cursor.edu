import matplotlib.pyplot as plt
from math import sin, pi
from numpy import array, arange, abs as np_abs
from numpy.fft import rfft, rfftfreq
import numpy as np
import math
import sys

def progressBar(value, endvalue, bar_length=20):

    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()

fd = 44100

with open("Current/low-high1.sd", "r") as f1:
    content1 = f1.read().splitlines()
with open("Current/filtred.sd", "r") as f6:
    content6 = f6.read().splitlines()

N1 = len(content1)
N6 = len(content6)

sound1 = []
sound6 = []

for i in range(N1):
	progressBar(i,N1)
	print(' Reading file low-high1.sd')
	sound1.append(float(content1[i]))
for i in range(N6):
	progressBar(i,N6)
	print(' Reading file filtred.sd')
	sound6.append(float(content6[i]))

x = [[],[]]

for i in range(N1):
	x[0].append(i/fd)
	progressBar(i,N1)
	print(' Reading file low-high1.sd')

for i in range(N6):
	x[1].append(i/fd)
	progressBar(i,N6)
	print(' Reading file filtred.sd')

y = [[],[]]

for i in range(N1):
	y[0].append(np.hamming(N1)[i])
	progressBar(i,N1)
	print(' Creating window 1')

for i in range(N6):
	y[1].append(np.hamming(N6)[i])
	progressBar(i,N6)
	print(' Creating window 2')

hmsound1 = []
hmsound6 = []

for i in range(N1):
	progressBar(i,N1)
	print('Creating window on low-high1.sd')
	hmsound1.append(sound1[i]*y[0][i])
for i in range(N6):
	progressBar(i,N6)
	print('Creating window on filter.sd')
	hmsound6.append(sound6[i]*y[1][i])

spectrum1 = rfft(hmsound1)
spectrum6 = rfft(hmsound6)

n = 25
kray1 = rfftfreq(N1, 1/fd)[len(rfftfreq(N1, 1/fd))-1]
nk = int(kray1/n)
frequncy = [[],[]]
amplitude = [[],[]]

ss = 0
n0 = 0
n1 = 0
for j in range(n):
	n1 += nk
	for i in range(n0,n1):
		progressBar(i,(n1-n0)*n)
		print('Creating histogram for low-high1.sd')
		ss += (np_abs(spectrum1)/N1)[i]
	amplitude[0].append(math.floor(ss))
	ss = 0
	frequncy[0].append(n1)
	n0 += nk

ss = 0
n0 = 0
n1 = 0
for j in range(n):
	n1 += nk
	for i in range(n0,n1):
		progressBar(i,(n1-n0)*n)
		print('Creating histogram for filter.sd')
		ss += (np_abs(spectrum6)/N6)[i]
	amplitude[1].append(math.floor(ss))
	ss = 0
	frequncy[1].append(n1)
	n0 += nk

plt.figure()
plt.subplot(321)
plt.grid()
plt.plot(x[0], hmsound1)
plt.xlabel('T')
plt.title('high.sd')
plt.subplot(322)
plt.grid()
plt.plot(x[1], hmsound6)
plt.title('filtred.sd')
plt.subplot(323)
plt.grid()
plt.plot(rfftfreq(N1, 1/fd), np_abs(spectrum1)/N1)
plt.subplot(324)
plt.grid()
plt.plot(rfftfreq(N6, 1/fd), np_abs(spectrum6)/N6)
plt.subplot(325)
plt.grid()
plt.bar(range(1,n+1),amplitude[0])
plt.subplot(326)
plt.grid()
plt.bar(range(1,n+1),amplitude[1])
plt.show()