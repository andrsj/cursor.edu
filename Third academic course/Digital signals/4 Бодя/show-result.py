import matplotlib.pyplot as plt
from math import sin, pi
from numpy import array, arange, abs as np_abs
from numpy.fft import rfft, rfftfreq
import numpy as np
import math

fd = 44100
v = 100000

with open("аа.txt", "r") as f1:
    content1 = f1.read().splitlines()
with open("ее.txt", "r") as f2:
    content2 = f2.read().splitlines()
with open("ии.txt", "r") as f3:
    content3 = f3.read().splitlines()
with open("оо.txt", "r") as f4:
    content4 = f4.read().splitlines()
with open("уу.txt", "r") as f5:
    content5 = f5.read().splitlines()
with open("result-recorder.txt", "r") as f6:
    content6 = f6.read().splitlines()

N1 = len(content1)
N2 = len(content2)
N3 = len(content3)
N4 = len(content4)
N5 = len(content5)
N6 = len(content6)

sound1 = []
sound2 = []
sound3 = []
sound4 = []
sound5 = []
sound6 = []

for i in range(N1):
	sound1.append(int(v*float(content1[i])))
for i in range(N2):
	sound2.append(int(v*float(content2[i])))
for i in range(N3):
	sound3.append(int(v*float(content3[i])))
for i in range(N4):
	sound4.append(int(v*float(content4[i])))
for i in range(N5):
	sound5.append(int(v*float(content5[i])))
for i in range(N6):
	sound6.append(int(v*float(content6[i])))

x = [[i/fd for i in range(N1)],[i/fd for i in range(N2)],[i/fd for i in range(N3)],[i/fd for i in range(N4)],[i/fd for i in range(N5)],[i/fd for i in range(N6)]]
y = [[np.hamming(N1)[i] for i in range(N1)],[np.hamming(N2)[i] for i in range(N2)],[np.hamming(N3)[i] for i in range(N3)],[np.hamming(N4)[i] for i in range(N4)],[np.hamming(N5)[i] for i in range(N5)],[np.hamming(N6)[i] for i in range(N6)]]

hmsound1 = []
hmsound2 = []
hmsound3 = []
hmsound4 = []
hmsound5 = []
hmsound6 = []

for i in range(N1):
	hmsound1.append(sound1[i]*y[0][i])
for i in range(N2):
	hmsound2.append(sound2[i]*y[1][i])
for i in range(N3):
	hmsound3.append(sound3[i]*y[2][i])
for i in range(N4):
	hmsound4.append(sound4[i]*y[3][i])
for i in range(N5):
	hmsound5.append(sound5[i]*y[4][i])
for i in range(N6):
	hmsound6.append(sound6[i]*y[5][i])

spectrum1 = rfft(hmsound1)
spectrum2 = rfft(hmsound2)
spectrum3 = rfft(hmsound3)
spectrum4 = rfft(hmsound4)
spectrum5 = rfft(hmsound5)
spectrum6 = rfft(hmsound6)

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

ss = 0
n0 = 0
n1 = 0
for j in range(n):
	n1 += nk
	for i in range(n0,n1):
		ss += (np_abs(spectrum2)/N2)[i]
	amplitude[1].append(math.floor(ss))
	ss = 0
	frequncy[1].append(n1)
	n0 += nk

ss = 0
n0 = 0
n1 = 0
for j in range(n):
	n1 += nk
	for i in range(n0,n1):
		ss += (np_abs(spectrum3)/N3)[i]
	amplitude[2].append(math.floor(ss))
	ss = 0
	frequncy[2].append(n1)
	n0 += nk

ss = 0
n0 = 0
n1 = 0
for j in range(n):
	n1 += nk
	for i in range(n0,n1):
		ss += (np_abs(spectrum4)/N4)[i]
	amplitude[3].append(math.floor(ss))
	ss = 0
	frequncy[3].append(n1)
	n0 += nk

ss = 0
n0 = 0
n1 = 0
for j in range(n):
	n1 += nk
	for i in range(n0,n1):
		ss += (np_abs(spectrum5)/N5)[i]
	amplitude[4].append(math.floor(ss))
	ss = 0
	frequncy[4].append(n1)
	n0 += nk

ss = 0
n0 = 0
n1 = 0
for j in range(n):
	n1 += nk
	for i in range(n0,n1):
		ss += (np_abs(spectrum6)/N6)[i]
	amplitude[5].append(math.floor(ss))
	ss = 0
	frequncy[5].append(n1)
	n0 += nk

plt.figure()

plt.subplot(361)
plt.grid()
plt.plot(x[0], hmsound1)
plt.xlabel('T')
plt.title('aa.txt')

plt.subplot(362)
plt.grid()
plt.plot(x[1], hmsound2)
plt.title('ee.txt')

plt.subplot(363)
plt.grid()
plt.plot(x[2], hmsound3)
plt.title('uu.txt')

plt.subplot(364)
plt.grid()
plt.plot(x[3], hmsound4)
plt.title('oo.txt')

plt.subplot(365)
plt.grid()
plt.plot(x[4], hmsound5)
plt.title('yy.txt')

plt.subplot(366)
plt.grid()
plt.plot(x[5], hmsound6)
plt.title('result-record.txt')

plt.subplot(367)
plt.grid()
plt.plot(rfftfreq(N1, 1/fd), np_abs(spectrum1)/N1)
plt.title('Спектр')

plt.subplot(368)
plt.grid()
plt.plot(rfftfreq(N2, 1/fd), np_abs(spectrum2)/N2)
plt.title('Спектр')

plt.subplot(369)
plt.grid()
plt.plot(rfftfreq(N3, 1/fd), np_abs(spectrum3)/N3)
plt.title('Спектр')

plt.subplot(3,6,10)
plt.grid()
plt.plot(rfftfreq(N4, 1/fd), np_abs(spectrum4)/N4)
plt.title('Спектр')

plt.subplot(3,6,11)
plt.grid()
plt.plot(rfftfreq(N5, 1/fd), np_abs(spectrum5)/N5)
plt.title('Спектр')

plt.subplot(3,6,12)
plt.grid()
plt.plot(rfftfreq(N6, 1/fd), np_abs(spectrum6)/N6)
plt.title('Гістограма')

plt.subplot(3,6,13)
plt.grid()
plt.bar(range(1,n+1),amplitude[0])
plt.title('Гістограма')

plt.subplot(3,6,14)
plt.grid()
plt.bar(range(1,n+1),amplitude[1])
plt.title('Гістограма')

plt.subplot(3,6,15)
plt.grid()
plt.bar(range(1,n+1),amplitude[2])
plt.title('Гістограма')

plt.subplot(3,6,16)
plt.grid()
plt.bar(range(1,n+1),amplitude[3])
plt.title('Гістограма')

plt.subplot(3,6,17)
plt.grid()
plt.bar(range(1,n+1),amplitude[4])
plt.title('Гістограма')

plt.subplot(3,6,18)
plt.grid()
plt.bar(range(1,n+1),amplitude[5])
plt.title('Гістограма')

plt.show()