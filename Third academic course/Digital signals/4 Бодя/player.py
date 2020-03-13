import pyaudio
import math
import numpy as np
import matplotlib.pyplot as plt

fd = 44100     
channels = 1

with open("result-recorder.txt", "r") as f:
    content = f.read().splitlines()

sound = []

for i in range(len(content)):
	sound.append(content[i])

a1 = np.array(sound)

y1 = a1.astype(np.float32).tobytes()

p = pyaudio.PyAudio()

stream1 = p.open(format=pyaudio.paFloat32, channels=channels, rate=fd, output=True)

print('Початок відігравання')
stream1.write(y1)
stream1.stop_stream()
print('Кінець')
stream1.close()

p.terminate()