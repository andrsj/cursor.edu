import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(x-2)
fx_name = r'$f(x)=\frac{1}{x-2}$'

# using 101 steps results in in array including the value 0
x=np.linspace(-10,10,10001)
# f(0) = nan -> a nan value creates a gap
y=f(x)
plt.plot(x, y, label=fx_name)
plt.legend(loc='upper left')
plt.grid()
plt.show()