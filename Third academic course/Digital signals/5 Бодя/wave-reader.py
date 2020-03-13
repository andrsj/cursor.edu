import scipy.io.wavfile
import matplotlib.pyplot as plt
import sys

def progressBar(value, endvalue, bar_length=20):

    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()

samplerate, data = scipy.io.wavfile.read("Tracks/low-high.wav")
N = len(data)
x = [i*(1/samplerate) for i in range(N)]
v = 10**8

d1 = open('Current/low-high1.sd', 'w')
d2 = open('Current/low-high2.sd', 'w')

dd1 = []
dd2 = []

for i in range(len(data)):
	print(' Writing start')
	progressBar(i,len(data))
	dd1.append(data[i][0])
	dd2.append(data[i][1])	
	d1.write(str(int(v*data[i][0])) + '\n')
	d2.write(str(int(v*data[i][1])) + '\n')
print(' Writing end')

d1.close()
d2.close()