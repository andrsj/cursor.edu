import random as rand
from collections import Counter
import matplotlib.pyplot as plt
import math


print("Перше завдання")
print("Створення масивів випадкових чисел")
x = []
# m = 7
m = 0.1 # математичне сподівання
# sigma = 1.5
sigma = 0.5 
N = 10000 # к-сть точок
# Цикл запису цих точок
i = 0
while i < N:
    eps = math.sqrt(12/5) * (sum([rand.uniform(0,1) for i in range(5)]) - 5/2)
#     x.append(math.ceil(m + sigma * (0.01 * eps * (97 + eps ** 2)) * 1000)/1000)
    x.append(m + sigma * (0.01 * eps * (97 + eps ** 2)))
    i += 1

print("Обчислення математичного сподівання і дисперсії генеральної вибірки N чисел")
# Математичне сподівання (обчислене) і Дисперсія
Mx = sum(x)/len(x)
Dx = sum(i*i for i in x)/len(x) - Mx**2
sigma_ = math.sqrt(Dx)

print(Mx, " -> Mx\t" , Dx, " -> Dx")

print("Обчислення математичного сподівання і дисперсії в залежності від N")
# Обчислення математичного сподівання і дисперсії в залежності від N
i = 100
MX = []
DX = []
SIGMA = []

# def MX(a = []):
# 	return sum(a)/len(a)

import sys
def progressBar(value, endvalue, bar_length=20):

    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()


while i <= N:
    Mx = sum(x[:i])/len(x[:i])
    MX.append(Mx)
    Dx = sum(i*i for i in x[:i])/len(x[:i]) - Mx**2
    DX.append(Dx)
    SIGMA.append(math.sqrt(Dx))
    i += 1
    progressBar(i,N)

progressBar(N,N)

plt.figure()
plt.plot([i for i in range(100,len(MX)+100)],MX)
plt.title("Залежність MX від N")
plt.grid()

# plt.figure()
# plt.plot([i for i in range(100,len(DX)+100)],DX)
# plt.title("Залежність DX від N")
# plt.grid()

plt.figure()
plt.plot([i for i in range(100,len(SIGMA)+100)],SIGMA)
plt.title("Залежність Sigma від N")
plt.grid()
plt.show()


print(" ")
print("Друге та третє завдання")
# Сортування значень випадкових чисел
count_items = Counter(x)
count_items_sort_keys = list(count_items.keys())
count_items_sort_keys.sort()
print("Створення масивів точок X та Y для графіка")
# Згруповування випадкових чисел у вхідний масив Х
a = []
OX = []
for i in count_items_sort_keys:
    a.append(i)
for i in a:
    OX.extend([i, i])

    
    
# Згруповування к-сті повторювань відповідних чисел у вхідний масив Y   
b = []
OY = [0,]
for i in count_items_sort_keys:
    b.append(count_items[i])
    
k = 1
c = []
while k <= len(b):
    c.append(sum(b[:k]))
    k += 1
    progressBar(k,len(b))
for i in c:
    OY.extend([i, i])
OY.pop()


# Емпіричний графік
plt.figure()
plt.plot(OX,OY)
plt.title("Емпіричний графік")
plt.grid()






print(" ")
print("Створення гістограми для масиву випадкових N чисел")
# Обчислення к-сті груп для гістограми
m = 1 + 3.334 * math.log(N,10)

print("m -> ", m , "\t N -> " , N)
print(math.log(N))

# Крок для однієї групи
h = ( max(count_items_sort_keys) - min(count_items_sort_keys) ) / m
d = [min(count_items_sort_keys),]
i = 1
while i <= m:
    d.append(min(count_items_sort_keys) + h * i)
    i += 1

# plt.figure()
# plt.hist(x,bins = d)
# plt.title("Гістограма")
# plt.show()

plt.figure()
plt.hist(x,bins = int(m))
plt.title("Гістограма")
plt.show()