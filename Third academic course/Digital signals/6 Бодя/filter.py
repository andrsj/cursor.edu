import matplotlib.pyplot as plt
from math import sin, pi, cos
from numpy import array, arange, abs as np_abs
from numpy.fft import rfft, rfftfreq
import numpy as np
import math

fd = 44100

with open("Current/a4shot2000.txt", "r") as f1:
    content = f1.read().splitlines()

N1 = len(content)

sound1 = []

for i in range(N1):
	sound1.append(int(content[i]))

fs = 2000
# fs = 4600
fn = fd/2
R = 1.01
w = pi*fs/fn
Re1 = cos(w)
Re2 = R*cos(w)
b0 = 1
b1 = -2*Re1
b2 = 1
a1 = (-2*Re2)/(R*R)
a2 = 1/R*R
a = [a1, a2]
b = [b0, b1, b2]
y = []

y.append(b[0]*sound1[0])
y.append(b[0]*sound1[0]+b[1]*sound1[0]-a[0]*y[0])

for i in range(2,N1):
	Y = b[0]*sound1[i]+b[1]*sound1[i-1]+b[2]*sound1[i-2]-a[0]*y[i-1]-a[1]*y[i-2]
	y.append(Y)

d = open('Current/filtred.txt', 'w')

print('Writing file')
for i in range(N1):
	d.write(str(int(y[i])) + '\n')	
print('Writing end')

d.close()