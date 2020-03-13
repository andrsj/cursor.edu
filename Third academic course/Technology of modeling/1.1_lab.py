import matplotlib.pyplot as plt

x = [0.1,]
k = 1
M = 104343


while k < 1000:
    x.append(M * x[k-1] - int(M * x[k-1]))
    k += 1

Mx = sum(x)/len(x)
Dx = sum(i*i for i in x)/len(x) - Mx**2
print("Середнє генеральної вибірки:\t"  + str(Mx))
print("Дисперсія генеральної вибірки:\t"  + str(Dx))

Dx_ = sum(i*i for i in x[:100]) / len(x[:100]) - (sum(x[:100])/len(x[:100]))**2
print("Дисперсія вибірки:\t\t" + str(Dx_))

L = [0]*10
for i in x:
    if i >= 0 and i <= 0.1:
        L[0] += 1
    elif i > 0.1 and i <= 0.2:
        L[1] += 1
    elif i > 0.2 and i <= 0.3:
        L[2] += 1
    elif i > 0.3 and i <= 0.4:
        L[3] += 1
    elif i > 0.4 and i <= 0.5:
        L[4] += 1
    elif i > 0.5 and i <= 0.6:
        L[5] += 1
    elif i > 0.6 and i <= 0.7:
        L[6] += 1
    elif i > 0.7 and i <= 0.8:
        L[7] += 1
    elif i > 0.8 and i <= 0.9:
        L[8] += 1
    elif i > 0.9 and i <= 1:
        L[9] += 1

interval = []
for i in range(10):
	interval.append([i/10,(i+1)/10])

print("\t|".join(str(i)[1:-1] for i in interval))
print("\t\t|".join(str(i) for i in L))
print("\t\t|".join(str(j) for j in (list(i/len(x) for i in L))))

plt.hist(x,bins = 10)
plt.grid()
plt.show()
