import math
import matplotlib.pyplot as plt
import random as rand
import collections

x = []
w = []
for i in range(100):
    x.append(rand.randint(-10,10))
    w.append(rand.random())

x.append(1)
w.append(0.1)

S = 0
Sum = [S,]
alpha = 0.7
OUT = 1 / (1 + math.exp( -alpha * S))
O = [OUT,]
for i in x:
    S += w[x.index(i)] * i
    Sum.append(S)
    O.append(1 / (1 + math.exp( -alpha * S)))


points = {i : j for i,j in zip(Sum,O)}
# for i in points:
#     print (i, points[i])

sortpoints = collections.OrderedDict(sorted(points.items()))
# for i in sortpoints:
#     print(i,sortpoints[i])

plt.plot([i for i in sortpoints],[sortpoints[i] for i in sortpoints])
plt.grid()
plt.show()

# plt.plot(Sum,O)
# plt.grid()
# plt.show()