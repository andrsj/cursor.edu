# files = open("output.txt", "w")
# files.write("lho70;;")
# files.close()

import math
import random as rand
import numpy as np
import matplotlib.pyplot as plt

def function_norm (x):
    return x**2


a = 10
k = -a
x = [k,]
y1 = [function_norm(x[0]),]
i = 0
while k<=a:
    x.append(k)
    k += 1
    i += 1
    y1.append(function_norm(float(x[i])))


plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x,y1)
plt.show()


o = 0
while o <= 21:
    print(str(x[o]) + "\t" + str(y1[o]) + "\n")
    o += 1