import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return math.sin(x)


a = math.pi
k = -a
x = [k,]
y = [f(x[0]),]
i = 0
while k<=a:
    k += 0.1
    i += 1
    x.append(k)
    y.append(f(float(x[i])))


plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x,y)
plt.show()

plus = []
minus = []
dictionary = dict(zip(x,y))
for key in dictionary:
    if dictionary[key] > 0:
        plus.append(dictionary[key])
    else:
        minus.append(dictionary[key])

file_for_plus = open("plus_output.txt","w")
file_for_minus = open("minus_output.txt","w")

j = 0
for i in plus:
    j += 1
    file_for_plus.write(str(i) + "\n")
file_for_plus.write("\n Plus:" + str(j) + "\n")

j = 0
for i in minus:
    j += 1
    file_for_minus.write(str(i) + "\n")
file_for_minus.write("\n Minus:" + str(j) + "\n")

file_for_plus.close()
file_for_minus.close()
