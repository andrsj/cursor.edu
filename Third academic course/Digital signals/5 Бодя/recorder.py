import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import scipy.io.wavfile
import matplotlib.pyplot as plt
import pyaudio
import wave

fd = 44100
duration = 1
channels = 1

print('\tReady?? (+/-)')

if '+' == input(): 
	myrecording = sd.rec(duration * fd, samplerate=fd, channels=channels,dtype='float32')

	print("Recording Audio")
	sd.wait()
	print('Recording end')

	N = len(myrecording)
	x = [i*(1/fd) for i in range(N)]
	d = open('Current/result-recorder.sd', 'w')

	date = []
	for i in range(len(myrecording)):
		date.append(myrecording[i][0])

	v = 10**8

	print('Writing file')
	for i in range(len(date)):
		d.write(str(int(v*date[i])) + '\n')	
	print('Writing end')
	d.close()

else:
	print('\tError!')