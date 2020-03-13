import matplotlib.pyplot as plt
import random as rand
import math

m = 0.1
sigma = 0.3
N = 25


def evklid2d(a = [],b = []):
    if a == b:
        return 666
    sum = 0
    for i,j in zip(a,b):
        sum += (i - j)**2
    return math.sqrt(sum)

def gen():
    eps = eps = math.sqrt(12/5) * (sum([rand.uniform(0,1) for i in range(5)]) - 5/2)
    return m + sigma * (0.01 * eps * (97 + eps ** 2))

data_0_0 = []
while (len(data_0_0) < 25):
    data_0_0.append([gen(),gen(),"r"])

data_1_1 = []
while (len(data_1_1) < 25):
    data_1_1.append([gen() + 1,gen() + 1,'g'])

data_3_1 = []
while (len(data_3_1) < 25):
    data_3_1.append([gen() + 3,gen() + 1, 'b'])





plt.figure()

for i in [[0,0],[1,1],[3,1]]:
    plt.scatter(i[0],i[1], color = "black")

for j in [data_0_0,data_1_1,data_3_1]:
    for i in j:
        plt.scatter(i[0],i[1], s = 5 , c = i[2])

plt.axvline(0)
plt.axhline(0)
plt.grid()








data = data_0_0 + data_1_1 + data_3_1
T = sigma




clusters = [
    {
        "xy" : [data[0][0], data[0][1]],
        "cluster" : [[data[0][0], data[0][1]],]
    },
]

for i in data:
    distances = []
    for j in clusters:
        distances.append(evklid2d(i,j["xy"]))

    # print(distances,'\t Дистанція')
    # print(min(distances),'\t мінімальна дистанція')
    # print(distances.index(min(distances)),'\t індекс мінімальної дистанції')
    # print(clusters[distances.index(min(distances))],'\t кластер, до якого відстань мінімальна')
    # print(clusters[distances.index(min(distances))]['xy'],'\t координата кластера')
    # print(clusters[distances.index(min(distances))]["cluster"],'\t кластер')

    if (min(distances) > T):
        clusters.append(
            {
                "xy" : [i[0],i[1]],
                "cluster" : [[i[0],i[1]],]
            }
        )
    else:
        clusters[distances.index(min(distances))]["cluster"].append([i[0],i[1]])









plt.figure()

for i in clusters:
    print(i)

for i in clusters:
    colors = [(rand.random(),rand.random(),rand.random())]
    for j in i['cluster']:
        plt.scatter(j[0],j[1], color = colors) #, s = 10)

for i in [[0,0],[1,1],[3,1]]:
    plt.scatter(i[0],i[1], color = "black")

plt.axvline(0)
plt.axhline(0)
plt.grid()




plt.show()
