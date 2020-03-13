import matplotlib.pyplot as plt
import math

x = [i for i in range(16)]
y = [	87 ,79  ,76.4,74.2,
		72.3,69.9,68.4,67.1,
		65.2,64  ,63  ,61.5,
		60.1,58.9,58  ,57   ]
r = [i/100 for i in range(10,50)]
T0 = y[0]
Ts = 57

def func(x,r):
	return (T0 - Ts ) * math.exp( - r * x ) + Ts

YY = []
for j in r:
	if j == 0:
		continue
	else:
		Y = []
		for i in x:
			Y.append(func(i,j))
		YY.append(Y)

plt.plot(x,y,label = "X")

point = 3
plt.text(8,80,"Точка порівняння: {}".format(point),bbox = dict(facecolor='red', alpha=0.5))

for i in range(len(YY)):
	delta = math.fabs((y[point] - YY[i][point]) / y[point])
	if 0.01 < delta < 0.1:
		plt.plot(x,YY[i],alpha = 0.35)
	elif delta <= 0.01:
		plt.plot(x,YY[i],alpha = 0.9, color = "r",label = "{}".format(r[i+1]))
	else:
		plt.plot(x,YY[i],alpha = 0.1)

plt.grid()
plt.legend()
plt.show()