import matplotlib.pyplot as plt
from math import sin, pi, ceil, fabs
from numpy import array, arange, abs as np_abs
from numpy.fft import rfft, rfftfreq
import numpy as np

f = 1000
fd = 44100
fnotu = 147
N = 100000
v = 10**2

garmoniks = [v*sin(2*pi*f*t/fd) for t in range(N)]
spectrum = rfft(garmoniks)
x = [i/fd for i in range(N)]

Am = max(spectrum)
df = fd/N

for i in range(len(rfftfreq(N, 1/fd))):
	if spectrum[i] == Am:
		Fm = rfftfreq(N, 1/fd)[i]

fdn = fabs(Fm - fnotu)

f = open('results.txt','w')
f.write("\nОкiл реальноi максимальноi частоти fm = "+str(ceil((Fm)*100)/100)+" = ("+str(ceil((Fm - df)*100)/100)+";"+str(ceil((Fm + df)*100)/100)+").")
f.write("\nЧастота максимальна тону гiтарноi ноти становить = "+str(fnotu)+".")
f.write("\nРеальна рiзниця становить = +/-"+str(ceil((fdn)*100)/100)+", теоретична = +/-"+str(df)+".\n")
f.close()

plt.figure()
plt.subplot(121)
plt.plot(x, garmoniks)
plt.xlabel('T')
plt.ylabel('F1(T)')
plt.title('Одна гармоніка')
plt.grid()
plt.subplot(122)
plt.plot(rfftfreq(N, 1/fd), np_abs(spectrum)/N)
plt.xlabel('Frq')
plt.ylabel('F1(T)')
plt.title('Одна гармоніка (спектр)')
plt.grid()
plt.show()
