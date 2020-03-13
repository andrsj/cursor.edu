import math
import random as rand
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return math.sqrt(x)


a = 10
k = 0
x = [k,]
y1 = [func(x[0]),]
i = 0
while k<=a:
    k += 0.1
    i += 1
    x.append(k)
    y1.append(func(float(x[i])))

b = [x[0],]
v = 1
print(len(y1))
while v <= len(y1)-1:
    b.append(b[v-1] + (1/v) * (y1[v] - b[v-1]))
    v += 1

plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x,y1)
plt.plot(x,b)
plt.show()