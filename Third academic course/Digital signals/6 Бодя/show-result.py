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

with open("Current/a4shot2000.txt", "r") as f1:
    content1 = f1.read().splitlines()
with open("Current/filtred.txt", "r") as f2:
    content2 = f2.read().splitlines()
with open("Current/huming.txt", "r") as f3:
    content3 = f3.read().splitlines()

N = len(content1)

sound1 = []
sound2 = []
huming = []

for i in range(N):
	progressBar(i,N)
	print(' Reading file text.txt')
	sound1.append(float(content1[i]))

for i in range(N):
	progressBar(i,N)
	print(' Reading file filtred.txt')
	sound2.append(float(content2[i]))

for i in range(N):
	progressBar(i,N)
	print(' Reading file filtred.txt')
	huming.append(float(content3[i]))

x = [[],[]]

for i in range(N):
	x[0].append(i/fd)
	progressBar(i,N)
	print(' Reading file text.txt')

for i in range(N):
	x[1].append(i/fd)
	progressBar(i,N)
	print(' Reading file filtred.sd')

hmsound1 = []
hmsound2 = []

for i in range(N):
	progressBar(i,N)
	print('Creating window on text.txt')
	hmsound1.append(sound1[i]*huming[i])

for i in range(N):
	progressBar(i,N)
	print('Creating window on filtred.txt')
	hmsound2.append(sound2[i]*huming[i])

spectrum1 = rfft(hmsound1)
spectrum2 = rfft(hmsound2)

plt.figure()
plt.subplot(221)
plt.grid()
plt.plot(x[0], hmsound1)
plt.xlabel('T')
plt.title('high.sd')
plt.subplot(222)
plt.grid()
plt.plot(x[1], hmsound2)
plt.title('filtred.sd')
plt.subplot(223)
plt.grid()
plt.plot(rfftfreq(N, 1/fd), np_abs(spectrum1)/N)
plt.subplot(224)
plt.grid()
plt.plot(rfftfreq(N, 1/fd), np_abs(spectrum2)/N)
plt.show()