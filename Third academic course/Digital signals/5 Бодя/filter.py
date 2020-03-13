import matplotlib.pyplot as plt
from math import sin, pi
from numpy import array, arange, abs as np_abs
from numpy.fft import rfft, rfftfreq
import numpy as np
import math

fd = 44100
v = 10**8

with open("Current/result-recorder.sd", "r") as f1:
    content1 = f1.read().splitlines()

N1 = len(content1)

sound1 = []

for i in range(N1):
	sound1.append(int(content1[i]))

# a = [0.097269,0.000000,-0.194539,0.000000,0.097269]
# b = [1.000000,-1.632420,1.645300,-0.894239,0.334126]

a = [0.292893, -0.585786, 0.292893]
b = [1.0,	   0.0		, 0.171573]

y = []
y.append(a[0]*sound1[0])
y.append(a[0]*sound1[0]+a[1]*sound1[0]-b[1]*y[0])
# y.append(a[0]*sound1[0]+a[1]*sound1[0]+a[2]*sound1[0]-b[1]*y[0]-b[2]*y[0])
# y.append(a[0]*sound1[0]+a[1]*sound1[0]+a[2]*sound1[0]+a[3]*sound1[0]-b[1]*y[0]-b[2]*y[0]-b[3]*y[0])

for i in range(2,N1):
	# Y = a[0]*sound1[i]+a[1]*sound1[i-1]+a[2]*sound1[i-2]+a[3]*sound1[i-3]+a[4]*sound1[i-4]-b[1]*y[i-1]-b[2]*y[i-2]-b[3]*y[i-3]-b[4]*y[i-4]
	Y = a[0] * sound1[i] + a[1] * sound1 [i-1] + a[2] * sound1[i-1] - b[1] * y[i-1] - b[2] * y[i-2]
	y.append(Y)

d = open('Current/filtred.sd', 'w')

y_new = [i * 20 for i in y]

print('Writing file')
for i in range(N1):
	d.write(str(int(y_new[i])) + '\n')	
print('Writing end')

d.close()