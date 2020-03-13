import scipy.io.wavfile
import matplotlib.pyplot as plt
import sys
import wave

with open("Current/filtred.sd", "r") as f1:
	content = f1.read().splitlines()
v = 10**8
sound = []
for i in range(len(content)):
	sound.append(float(content[i])/v)

RATE = 44100
sample_width = len(sound)

wf = wave.open('Current/high1', 'wb')
wf.setnchannels(1)
wf.setframerate(RATE)
wf.writeframes(sound)
wf.close()