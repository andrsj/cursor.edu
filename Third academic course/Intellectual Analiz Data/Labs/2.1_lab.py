import math
import random as rand
import numpy as np
import matplotlib.pyplot as plt


def function (x):
    return math.sin(0.1*x) + math.sin(x) + rand.uniform(0,0.5)

def function_norm (x):
    return math.sin(0.1*x) + math.sin(x)



a = 100
k = -a
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


plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,b)
plt.show()


# Независимая (x) и зависимая (y) переменные
# x = np.linspace(0, 10, 50)
# y1 = x
# y2 = [i**2 for i in x]
# Построение графика

# plt.title("Линейная зависимость y = x") # заголовок

# plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# plt.plot(x, y "r--")  # построение графика
# plt.plot(x , y1 , x , y2)  # построение графика