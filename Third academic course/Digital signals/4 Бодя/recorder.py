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
myrecording = sd.rec(duration * fd, samplerate=fd, channels=channels,dtype='float32')

print("Запис аудіо")
sd.wait()
print('Кінець запису')


N = len(myrecording)
x = [i*(1/fd) for i in range(N)]
d = open('result-recorder.txt', 'w')

date = []

for i in range(len(myrecording)):
	date.append(myrecording[i][0])

print('Запис у файл')
for i in range(len(date)):
	d.write(str(date[i]) + '\n')
print('Кінець запису')

d.close()