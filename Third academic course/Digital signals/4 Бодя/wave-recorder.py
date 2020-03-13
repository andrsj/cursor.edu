import scipy.io.wavfile
import matplotlib.pyplot as plt

samplerate, data = scipy.io.wavfile.read("voice.wav")
N = len(data)
x = [i*(1/samplerate) for i in range(N)]

plt.figure()
plt.plot(x,data)
plt.show()

d = open('result-record.txt', 'w')

for i in range(len(data)):
	d.write(str(int(data[i])) + '\n')

d.close()
