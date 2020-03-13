import random as rand
import math
import matplotlib.pyplot as plt
import numpy
from scipy.cluster.hierarchy import linkage, dendrogram

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
    

data = data_0_0 + data_1_1 + data_3_1
dat = []
for i in data:
    # print(i)
    dat.append([i[0],i[1]])

    
r = "r"*25
g = 'g'*25
b = "b"*25
target = r + g + b

plt.figure()

mergings = linkage(dat,method='single')
# print(mergings)

for i in mergings:
    print(i[0],'\t',i[1],'\t',i[2],'\t',i[3])

R = dendrogram(mergings, labels=[
    i for i in target
    ], orientation = 'left', leaf_font_size = 10)

plt.figure()
counter = 1
for i,j in zip(dat,target):
    plt.scatter(i[0],i[1], c = j)
    plt.text(i[0],i[1], s = str(counter) , fontsize = 10)
    counter += 1

plt.show()