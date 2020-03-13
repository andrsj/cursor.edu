import matplotlib.pyplot as plt
import random as rand

X = []
Y = []
R = [0,0]

def func(x):
	if 0 <= x < 2:
		return 0.125 * x
	elif 2 <= x < 4:
		return 0.125 * x - 0.25
	elif 4 <= x < 6:
		return 0.125 * x - 0.5
	elif 6 <= x <= 8:
		return 0.125 * x - 0.75
	else:
		return None

QQ = []

while len(QQ) < 2000:
	R = [rand.random() * 8 , rand.random() * 0.25]

	if R[1] > func(R[0]):
		continue
	else:
		QQ.append([R[0],R[1]])


QQQ = []
for i in QQ:
	QQQ.append(i[0])

Mx = sum(QQQ)/len(QQQ)
Dx = sum(i*i for i in QQQ)/len(QQQ) - Mx**2
print("Mx -> " , Mx)
print("Dx -> " , Dx)




h = abs(0 - 8) / 10
interval = []
for i in range(10):
	interval.append([0+h*i, h+h*i])


L = [0] * 10
for i in QQQ:
	if i >= interval[0][0] and i<=interval[0][1]:
		L[0] += 1
	if i >= interval[1][0] and i<=interval[1][1]:
		L[1] += 1
	if i >= interval[2][0] and i<=interval[2][1]:
		L[2] += 1
	if i >= interval[3][0] and i<=interval[3][1]:
		L[3] += 1
	if i >= interval[4][0] and i<=interval[4][1]:
		L[4] += 1
	if i >= interval[5][0] and i<=interval[5][1]:
		L[5] += 1
	if i >= interval[6][0] and i<=interval[6][1]:
		L[6] += 1
	if i >= interval[7][0] and i<=interval[7][1]:
		L[7] += 1
	if i >= interval[8][0] and i<=interval[8][1]:
		L[8] += 1
	if i >= interval[9][0] and i<=interval[9][1]:
		L[9] += 1

# print(L)
print('\t'.join(str(i)[1:-1] for i in interval))
print("\t\t|".join(str(i) for i in L))
print("\t\t|".join(str(j) for j in (list(i/len(QQQ) for i in L))))

print(sum(L))

plt.figure()
for i in QQ:
	plt.scatter(i[0],i[1])

plt.plot([0,2,2,4,4,6,6,8,8],[0,0.25,0,0.25,0,0.25,0,0.25,0], color = "b")
plt.grid()

plt.figure()
plt.hist(QQQ,bins=30)
plt.show()