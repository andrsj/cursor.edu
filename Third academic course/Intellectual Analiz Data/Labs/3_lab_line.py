import math
import random as rand
import numpy as np
import matplotlib.pyplot as plt


def function1 (x):
    return 8 - 2*x + rand.uniform(0,0.5)
def function2 (x):
    return 8 - 2*x + 10 * rand.uniform(0,0.5)
def function3 (x):
    return 8 - 2*x + 100 * rand.uniform(0,0.5)

def function_norm (x):
    return 8 - 2*x



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



r = [0,0,0,0]
for i in range(len(x)):
	r[0] += x[i] * y[0][i]
	r[1] += x[i] * y[1][i]
	r[2] += x[i] * y[2][i]
	r[3] += x[i] * y[3][i]

a2,a1 = ([],[])

for i in range(4):
	a2.append(  (len(x) * r[i] - sum(x) * sum (y[i])) / ( len(x) * sum([i*i for i in x]) - sum(x) * sum(x) )  )
	a1.append(  (sum(y[i]) * sum([i*i for i in x]) - r[i] * sum(x)) / ( len(x) * sum([i*i for i in x]) - sum(x) * sum(x) )  )

# for i in a2:
# 	print(i)

# for i in a1:
# 	print(i)

y.append([])
y.append([])
y.append([])
y.append([])

for i in x:
	y[4].append(a2[0] * i + a1[0])
	y[5].append(a2[1] * i + a1[1])
	y[6].append(a2[2] * i + a1[2])
	y[7].append(a2[3] * i + a1[3])


print("-"*97)
print("\t Вихідна \t|\t\t\tЛінійна емпірична функція\t\t\t|")
print("\t функція \t|\tАльфа = 1\t|\tАльфа = 10\t|\tАльфа = 100\t|")
print("-"*97)
print("\t Значення\t|\t\t\t|\t\t\t|\t\t\t|")
print("-"*97)
print(" a1\t|\t{:.4f}\t|\t{:.4f}\t\t|\t{:.4f}\t\t|\t{:.4f}\t\t|".format(a1[0],a1[1],a1[2],a1[3]))
print(" a2\t|\t{:.4f}\t|\t{:.4f}\t\t|\t{:.4f}\t\t|\t{:.4f}\t\t|".format(a2[0],a2[1],a2[2],a2[3]))
print("-"*97)




delta = [[],[]]
for i in range(4):
	delta[0].append(abs( a1[0] - a1[i] ) / a1[0])
	delta[1].append(abs( a2[0] - a2[i] ) / a2[0])

print(" a1\t|\t{:.3%}\t|\t{:.3%}\t\t|\t{:.3%}\t\t|\t{:.3%}\t|".format(
	delta[0][0],delta[0][1],delta[0][2],delta[0][3]))
print(" a2\t|\t{:.3%}\t|\t{:.3%}\t\t|\t{:.3%}\t\t|\t{:.3%}\t\t|".format(
	delta[1][0],delta[1][1],delta[1][2],delta[1][3]))
print("-"*97)



plt.figure()
plt.suptitle(" 8 - 2*x ")
plt.subplot(221)
plt.plot(x,y[0])
plt.plot(x,y[4])
plt.grid()

plt.subplot(222)
plt.plot(x,y[1])
plt.plot(x,y[5])
plt.grid()

plt.subplot(223)
plt.plot(x,y[2])
plt.plot(x,y[6])
plt.grid()

plt.subplot(224)
plt.plot(x,y[3])
plt.plot(x,y[7])
plt.grid()

plt.show()

# plt.plot(x,y[0])
# plt.plot(x,y[3])
# plt.plot(x,y[7])
# plt.grid()
# plt.show()
