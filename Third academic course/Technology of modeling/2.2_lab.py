import matplotlib.pyplot as plt
import math

h = [15/60,10/60,5/60]
r = 0.16
T0 = 82
Ts = 23
n = 110
t = [i * h[0] for i in range(n)]
Ts_ = []
T = []
TY = [[],[],[]]


def Euler (x,y,h):
  z = y
  z += h * function(x,z)
  return z

def function(x,y):
  r = 0.16
  Ts = 23
  return -r*(y-Ts)*x

def func(x):
	return (T0-Ts)*math.exp(-r*x)+Ts

for i in t:
  Ts_.append(23)

for i in t:
  T.append(func(i))

for i in range(n):
  TY[0].append(Euler(t[i],T[i],h[0]))
  TY[1].append(Euler(t[i],T[i],h[1]))
  TY[2].append(Euler(t[i],T[i],h[2]))

plt.figure(figsize = (12,6))

plt.text(12,60,'Крок аналітичної функції h = {}'.format(h[0]) , fontsize = 12 , bbox = dict(fc="none"))
plt.text(12,55,'В момент чау t = {}'.format(t[40]) , fontsize = 12 , bbox = dict(fc="none"))

htext = ["15/60","10/60","5/60"]

for i in range(3):
  plt.text(12,50 - i * 5,'Похибка при: h = {}    -->    {:.3%}'.format(
  	htext[i], math.fabs( (T[40]- TY[i][40] ) / T[40]) ) , fontsize = 12 , bbox = dict(facecolor='red', alpha=0.5))




plt.title("")
plt.xlabel("t хвилина")
plt.ylabel("T температура")

plt.scatter(t[40],T[40],color = "b")
plt.scatter(t[40],TY[0][40],color = "r")
plt.scatter(t[40],TY[1][40],color = "c")
plt.scatter(t[40],TY[2][40],color = "m")

plt.plot(t,T,label = "Аналітично розв'язане рівняння",color = "b")
plt.plot(t,Ts_)
plt.plot(t,TY[0], label = "h = 15 сек",color = "r")
plt.plot(t,TY[1], label = "h = 10 сек",color = "c")
plt.plot(t,TY[2], label = "h = 5 сек",color = "m")

# plt.xlim(-10,30)
plt.grid()
plt.legend()
plt.show()