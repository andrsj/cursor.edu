import matplotlib.pyplot as plt
import random as rand
import math

clusters_coord = [[0,0],[1,1],[3,1]]

x = []
m = 0.5
sigma = 1.5
N = 500
i = 0
while i < N:
    eps = math.sqrt(12/5) * (sum([rand.uniform(0,1) for i in range(5)]) - 5/2)
    x.append(m + sigma * (0.01 * eps * (97 + eps ** 2)))
    i += 1
y = []
i = 0
while i < N:
    eps = math.sqrt(12/5) * (sum([rand.uniform(0,1) for i in range(5)]) - 5/2)
    y.append(m + sigma * (0.01 * eps * (97 + eps ** 2)))
    i += 1
xy = []
for i,j in zip(x,y):
    xy.append([i,j])





def evklid2d(a = [],b = []):
    if a == b:
        return 666
    sum = 0
    for i,j in zip(a,b):
        sum += (i - j)**2
    return math.sqrt(sum)



distances = []
for i in xy:
    distance = []
    for j in clusters_coord:
        distance.append(evklid2d(i,j))
    distances.append(distance)

XY = []
for i,j in zip(xy,distances):
    clust = 0
    if j.index(min(j)) == 1:
        clust = 1
    if j.index(min(j)) == 2:
        clust = 2
    XY.append([i,clust])






for i in clusters_coord:
    plt.scatter(i[0],i[1], c = "black")

for i in XY:
    if i[1] == 0:
        plt.scatter(i[0][0], i[0][1] , c = "r", s = 5)
    elif i[1] == 1:
        plt.scatter(i[0][0], i[0][1] , c = "g", s = 5)
    else:
        plt.scatter(i[0][0], i[0][1] , c = "b", s = 5)

plt.axvline(0)
plt.axhline(0)
plt.grid()
plt.show()