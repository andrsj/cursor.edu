import pyaudio
import math
import numpy as np
import matplotlib.pyplot as plt

# p = pyaudio.PyAudio()

fd = 88200   
f = 500  
t = 0.004       
v = 100

y = (v*np.sin(2*np.pi*np.arange(fd*t)*f/fd)).astype(np.float32)
# stream = p.open(format=pyaudio.paFloat32, channels=2, rate=fd, output=True)

# stream.write(y)
# stream.stop_stream()
# stream.close()
# p.terminate()

x = [0]
td = t*fd
i = 1
xd = 0

while i < td:
	xd += 1/fd
	i += 1
	x.append(xd)

cy = [0]
k = 1

while k < td:
	b = round(y[k])
	cy.append(b)
	k += 1

print('Rewrite binary.txt \n')
print('Rewrite tens.txt \n')
print('Build function sin(t), only (d,k) \n')

plt.ioff()

fig, ax = plt.subplots()

ax.plot(x, cy, 'b', linestyle='solid')

lgnd = ax.legend(['sin(t)'], loc='upper center', shadow=False)
lgnd.get_frame().set_facecolor('#ffb19a')

plt.show()

f = open('binary.txt', 'w')
for i in range(len(cy)):
	b = ''
	n = int(cy[i])

	if n == 0:
		f.write(str(n))

	while n > 0:
		b = str(n % 2) + b
		n = n // 2

	f.write(b + '\n')

f.close()

d = open('tens.txt', 'w')

for i in range(len(cy)):
	d.write(str(int(cy[i])) + '\n')

d.close()
