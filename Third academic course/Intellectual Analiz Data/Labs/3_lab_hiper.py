import math
import random as rand
import numpy as np
import matplotlib.pyplot as plt


def function1 (x):
    # return -3 * x**2 + 5 * x - 4 + rand.uniform(0,0.5)
    return x - 0.9 * x**2 + rand.uniform(0,0.5)
def function2 (x):
    # return -3 * x**2 + 5 * x - 4 + 10 * rand.uniform(0,0.5)
    return x - 0.9 * x**2 + 10 * rand.uniform(0,0.5)
def function3 (x):
    # return -3 * x**2 + 5 * x - 4 + 100 * rand.uniform(0,0.5)
    return x - 0.9 * x**2 + 100 * rand.uniform(0,0.5)

def function_norm (x):
    # return -3 * x**2 + 5 * x - 4
    return x - 0.9 * x**2



a = 5
z = -a
x = [z,]
y = [[function_norm(x[0])] , [function1(x[0])] , [function2(x[0])] , [function3(x[0])]]

j = 0
while z<=a:
    z += 0.1
    j += 1
    x.append(z)
    y[0].append(function_norm(float(x[j])))
    y[1].append(function1(float(x[j])))
    y[2].append(function2(float(x[j])))
    y[3].append(function3(float(x[j])))

HH = []


for j in range(4):
    r2 = 0
    for i in range(len(x)):
    	r2 += x[i] * y[j][i]

    r1 = 0
    for i in range(len(x)):
        r1 += x[i] * x[i] * y[j][i]



    F = np.array([
        [sum([i**4 for i in x]),sum([i**3 for i in x]),sum([i**2 for i in x])],
        [sum([i**3 for i in x]),sum([i**2 for i in x]),sum(x)],
        [sum([i**2 for i in x]),sum(x),len(x)]
        ])
    G = np.array([
        r1,
        r2,
        sum(y[j])])

    H = np.linalg.solve(F,G)
    HH.append(H)


y.append([])
y.append([])
y.append([])
y.append([])

for i in x:
    y[4].append(HH[0][0] * i**2 + HH[0][1] * i + HH[0][2])
    y[5].append(HH[1][0] * i**2 + HH[1][1] * i + HH[1][2])
    y[6].append(HH[2][0] * i**2 + HH[2][1] * i + HH[2][2])
    y[7].append(HH[3][0] * i**2 + HH[3][1] * i + HH[3][2])




print("-" * 97)
print("\tВихідна   \t|\t\t Квадратична емпірична формула\t\t\t\t|")
print(" \tфункція   \t|\talpha = 1\t|\talpha = 10\t|\talpha = 100\t|")
print("-" * 97)
print(" \tЗначення  \t|\t\t\t|\t\t\t|\t\t\t|")
print("-" * 97)
print(" a1\t| {:.5f}\t|\t{:.6f}\t|\t{:.6f}\t|\t{:.6f}\t|".format(HH[0][2],HH[1][2],HH[2][2],HH[3][2]))
print(" a2\t| {:.5f}\t|\t{:.6f}\t|\t{:.6f}\t|\t{:.6f}\t|".format(HH[0][1],HH[1][1],HH[2][1],HH[3][1]))
print(" a3\t| {:.5f}\t|\t{:.6f}\t|\t{:.6f}\t|\t{:.6f}\t|".format(HH[0][0],HH[1][0],HH[2][0],HH[3][0]))
print("-" * 97)
print(" Значення похибки в %  \t|\t\t\t|\t\t\t|\t\t\t|")
print("-" * 97)


delta = [[],[],[]]
for i in range(4):
	delta[0].append(abs( HH[0][0] - HH[i][0] ) / HH[0][0])
	delta[1].append(abs( HH[0][1] - HH[i][1] ) / HH[0][1])
	delta[2].append(abs( HH[0][2] - HH[i][2] ) / HH[0][2])


print(" a1\t| {:.4%}\t|\t{:.4%}  \t|\t{:.4%}  \t|\t{:.4%}  \t|".format(
	delta[2][0],delta[2][1],delta[2][2],delta[2][3]))
print(" a2\t| {:.4%}\t|\t{:.4%}  \t|\t{:.4%}  \t|\t{:.4%}  \t|".format(
	delta[1][0],delta[1][1],delta[1][2],delta[1][3]))
print(" a3\t| {:.4%}\t|\t{:.4%}  \t|\t{:.4%}  \t|\t{:.4%}  \t|".format(
	delta[0][0],delta[0][1],delta[0][2],delta[0][3]))
print("-" * 97)



plt.figure()
plt.suptitle(" -3 * x^2 + 5 * x - 4 ")
plt.subplot(221)
plt.plot(x,y[0])
plt.plot(x,y[4])
plt.grid()

plt.subplot(222)
plt.plot(x,y[0])

plt.plot(x,y[1])
plt.plot(x,y[5])
plt.grid()

plt.subplot(223)
plt.plot(x,y[0])

plt.plot(x,y[2])
plt.plot(x,y[6])
plt.grid()

plt.subplot(224)
plt.plot(x,y[0])

plt.plot(x,y[3])
plt.plot(x,y[7])
plt.grid()

plt.show()

# plt.plot(x,y[0])
# plt.plot(x,y[3])
# plt.plot(x,y[7])
# plt.grid()
# plt.show()