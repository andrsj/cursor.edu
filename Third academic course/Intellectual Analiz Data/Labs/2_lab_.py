import math
import random as rand
import numpy as np
import matplotlib.pyplot as plt


def function (x):
    return math.sin(0.1*x) + math.sin(x) + rand.uniform(0,0.5)

def function_norm (x):
    return math.sin(0.1*x) + math.sin(x)



a = 100
k = 0
x = [k,]
y1 = [function_norm(x[0]),]
y2 = [function(x[0]),]
i = 0
while k<=a:
    k += 0.1
    i += 1
    x.append(k)
    y1.append(function_norm(float(x[i])))
    y2.append(function(float(x[i])))

b = [y2[0],]
v = 1 
while v <= len(y2)-1:
    b.append(b[v-1] + (1/v) * (y2[v] - b[v-1]))
    v += 1

plt.figure()
plt.xlabel("x")
plt.ylabel("y")
plt.grid()      
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,b)



o = 1
alpha = 0.1
b = [y2[0] + (y2[1] - y2[0]) * alpha]
while o < len(y2):
    b.append(alpha * y2[o-1] + (1 - alpha) * b[o-1])
    o += 1

del b[0]
b.append(y2[-2] + (y2[-1] - y2[-2]) * alpha)

plt.figure()
plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,b)
plt.show()

