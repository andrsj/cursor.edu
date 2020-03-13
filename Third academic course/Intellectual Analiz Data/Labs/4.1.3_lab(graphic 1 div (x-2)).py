import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(x-2)

x=np.linspace(-4,4,10001)
y=f(x)

plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x,y)
# plt.plot(x,y2)
plt.show()
