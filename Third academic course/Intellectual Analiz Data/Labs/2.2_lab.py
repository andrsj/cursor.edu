import math
import random as rand
import numpy as np
import matplotlib.pyplot as plt


def function (x):
    return math.sin(0.1*x) + math.sin(x) + rand.uniform(0,0.5)

def function_norm (x):
    return math.sin(0.1*x) + math.sin(x)


L = 3
a = 100
z = -a
x = [z,]
y1 = [function_norm(x[0]),]
y2 = [function(x[0]),]
j = 0
while z<=a:
    z += 0.1
    j += 1
    x.append(z)
    y1.append(function_norm(float(x[j])))
    y2.append(function(float(x[j])))



plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x,y1)
plt.plot(x,y2)
# plt.plot(x,b)
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