import matplotlib.pyplot as plt
import random as rand
import math

clusters_coord = [[0,0],[1,1],[3,1]]
clusters_points = [[],[],[]]
m = 0.5
sigma = 1.5





def evklid2d(a = [],b = []):
    if a == b:
        return 666
    sum = 0
    for i,j in zip(a,b):
        sum += (i - j)**2
    return math.sqrt(sum)

i1,i2,i3 = (0,0,0)
while(True):
    eps = math.sqrt(12/5) * (sum([rand.uniform(0,1) for i in range(5)]) - 5/2)
    x = (m + sigma * (0.01 * eps * (97 + eps ** 2)))
    eps = math.sqrt(12/5) * (sum([rand.uniform(0,1) for i in range(5)]) - 5/2)
    y = (m + sigma * (0.01 * eps * (97 + eps ** 2)))
    distance = [evklid2d([x,y],clusters_coord[0]),
                evklid2d([x,y],clusters_coord[1]),
                evklid2d([x,y],clusters_coord[2])]


    if (distance.index(min(distance)) == 0):
        if len(clusters_points[0]) < 25:
            clusters_points[0].append([x,y])
            i1 += 1
            print(i1)
    elif (distance.index(min(distance)) == 1):
        if len(clusters_points[1]) < 25:
            clusters_points[1].append([x,y])
            i2 += 1
            print('\t',i2)
    else:
        if len(clusters_points[2]) < 25:
            clusters_points[2].append([x,y])
            i3 += 1
            print('\t\t',i3)

    if(len(clusters_points[0]) == 25 and len(clusters_points[1]) == 25 and len(clusters_points[2]) == 25):
        break



for i in clusters_points[0]:
    plt.scatter(i[0],i[1], c = "red", s = 5)
for i in clusters_points[1]:
    plt.scatter(i[0],i[1], c = "blue", s = 5)
for i in clusters_points[2]:
    plt.scatter(i[0],i[1], c = "green", s = 5)

for i in clusters_coord:
    plt.scatter(i[0],i[1], c = "black")

print(len(clusters_points[0]), "\t - Перший")
print(len(clusters_points[1]), "\t - Другий")
print(len(clusters_points[2]), "\t - Третій")

plt.axvline(0)
plt.axhline(0)
plt.grid()
plt.show()