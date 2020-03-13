import matplotlib.pyplot as plt
from math import sin, pi
from numpy import array, arange, abs as np_abs
from numpy.fft import rfft, rfftfreq
import numpy as np
import math

with open("Current/a4shot2000.txt", "r") as f:
    content = f.read().splitlines()

y = []
N = len(content) 

for i in range(N):
	y.append(np.hamming(N)[i])
	print(' Creating window')

d = open('Current/huming.txt', 'w')

print('Writing file')
for i in range(N):
	d.write(str(y[i]) + '\n')	
print('Writing end')

d.close()