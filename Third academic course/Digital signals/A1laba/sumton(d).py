import pyaudio
import math
import numpy as np
import matplotlib.pyplot as plt

p = pyaudio.PyAudio()

fd = 88200   
f = 500  
t = 1       
v = 100

with open("tens1.txt", "r") as f1:
    content1 = f1.read().splitlines()

y = (v*(np.sin(2*np.pi*np.arange(fd*t)*f/fd)+np.cos(2*np.pi*np.arange(fd*t)*f*10/fd))).astype(np.float32)
stream = p.open(format=pyaudio.paFloat32, channels=2, rate=fd, output=True)

stream.write(y)
stream.stop_stream()
stream.close()
p.terminate()

x = [0]
td = t*fd
i = 1
xd = 0

while i < td:
	xd += 1/fd
	i += 1
	x.append(xd)

print('Build function sin(t), only (d) \n')

plt.ioff()

fig, ax = plt.subplots()

ax.plot(x, y, 'b', linestyle='solid')

lgnd = ax.legend(['sin(t) + cos(t) (d)'], loc='upper center', shadow=False)
lgnd.get_frame().set_facecolor('#ffb19a')

plt.show()

import pyaudio
import math
#!/usr/bin/env python
#coding=utf8
from numpy import array, arange, abs as np_abs
from numpy.fft import rfft, rfftfreq
from numpy.random import uniform
from math import sin, pi
import matplotlib.pyplot as plt
spectrum = rfft(y)

# когда закроется этот график, откроется следующий
# Потом спектр
plt.plot(rfftfreq(int(t*fd), 1/fd), np_abs(spectrum)/(int(t*fd)), 'g')
# rfftfreq сделает всю работу по преобразованию номеров элементов массива в герцы
# нас интересует только спектр амплитуд, поэтому используем abs из numpy (действует на массивы поэлементно)
# делим на число элементов, чтобы амплитуды были в милливольтах, а не в суммах Фурье. Проверить просто — постоянные составляющие должны совпадать в сгенерированном сигнале и в спектре
plt.xlabel(u'Частота, Гц')
plt.ylabel(u'Напряжение, мВ')
plt.title(u'Спектр')
plt.grid(True)
plt.show()