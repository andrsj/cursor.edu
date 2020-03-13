import matplotlib.pyplot as plt
import numpy

x = numpy.linspace(-20,20,200)
y = [(1 / (1 + numpy.exp(-0.3 * i))) for i in x]

plt.plot(x,y)
plt.grid()
plt.show()