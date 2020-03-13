import scipy.io.wavfile
import matplotlib.pyplot as plt

samplerate = 44100    

with open("result-recorder.txt", "r") as f:
    content = f.read().splitlines()

sound = []

v = 10**3

for i in range(len(content)):
	sound.append(int(v*float(content[i])))

N = len(content)
x = [i*(1/samplerate) for i in range(N)]

plt.figure()
plt.plot(x,sound)
plt.show()