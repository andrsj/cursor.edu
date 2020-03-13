import matplotlib.pyplot as plt

x = [1    ,4    ,12   ,16   ,25   ,33   ,37   ]
p = [0.05 ,0.25 ,0.25 ,0.15 ,0.13 ,0.1 ,0.07  ]

print("")
for i in range(len(x)):
	print('x['+str(i)+'] --> '+str(x[i])+'\tp['+str(i)+'] --> '+str(p[i]))

Mx = sum(x)/len(x)
Dx = sum(i*i for i in x)/len(x) - Mx**2
print("")
print("Mx -> ", Mx)
print("Dx -> ", Dx)

print("")
print("X\tCount\t P[X]")
print("*"*22)
for i in range(len(x)):
	print(x[i],"\t",int(p[i]*100),"\t",p[i])
print("*"*22)

plt.bar(x,p)
plt.show()

OX = [-10,]
OY = [0,0,]

for i in x:
	OX.extend([i,i])
Trash = []

for i in p:
	Trash.append(i)
k = 1
trash = []
while k <= len(Trash):
	trash.append(sum(Trash[:k]))
	k += 1

for i in trash:
	OY.extend([i,i])

# OY.pop()
OX.append(OX[-1]+10)

print(OX)
print(OY)

# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.yaxis.grid(linewidth = 10)

plt.plot(OX,OY)
plt.grid()
plt.show()