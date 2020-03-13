import pyaudio
import math
import numpy as np
import matplotlib.pyplot as plt

fd = 44100     
channels = 1
v = 10**8

print('\tReady?? (+/-)')

if input() == '+':
	print('\tWhat play?')
	text=input()

	if text == "f":
		with open("Current/filtred.sd", "r") as f1:
			content = f1.read().splitlines()
	elif text == "non-f":
		with open("Current/result-recorder.sd", "r") as f2:
			content = f2.read().splitlines()
	else:
		print('\tError!')
	
	sound = []

	for i in range(len(content)):
		sound.append(float(content[i])*2/v)

	a1 = np.array(sound)
	y1 = a1.astype(np.float32).tobytes()
	
	p = pyaudio.PyAudio()

	stream1 = p.open(format=pyaudio.paFloat32, channels=channels, rate=fd, output=True)

	print(' Start play')

	stream1.write(y1)
	stream1.stop_stream()
	print(' End play')
	stream1.close()
	p.terminate()

else:
	print('\tError!')
