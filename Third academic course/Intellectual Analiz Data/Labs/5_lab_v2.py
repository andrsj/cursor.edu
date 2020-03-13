import random as rand
from collections import Counter
import matplotlib.pyplot as plt
import math
x = []
i = 0 # ітератор
m = 0.1 # математичне сподівання
sigma = 0.5 
N = 10000 # к-сть точок
# Цикл запису цих точок
while i < N:
    eps = math.sqrt(12/5) * (sum([rand.uniform(0,1) for i in range(5)]) - 5/2)
#     x.append(math.ceil(m + sigma * (0.01 * eps * (97 + eps ** 2)) * 1000)/1000)
    x.append(m + sigma * (0.01 * eps * (97 + eps ** 2)))
    i += 1
# Математичне сподівання (обчислене)
Mx = sum(x)/len(x)
# Дисперсія
Dx = sum(i*i for i in x)/len(x) - Mx**2

# Сортування значень випадкових чисел
count_items = Counter(x)
count_items_sort_keys = list(count_items.keys())
count_items_sort_keys.sort()

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
for i in c:
    OY.extend([i, i])
OY.pop()


# Емпіричний графік
plt.figure()
plt.plot(OX,OY)
plt.grid()
# plt.show()

# Обчислення к-сті груп для гістограми
m = 1 + 3.334 * math.log(N)

# Гістограма
plt.figure()
plt.hist(x,bins = int(m))
# plt.show()	

# Крок для однієї групи
h = ( max(count_items_sort_keys) - min(count_items_sort_keys) ) / m
d = [min(count_items_sort_keys),]
i = 1
while i <= m:
    d.append(min(count_items_sort_keys) + h * i)
    i += 1

# Гістограма
plt.figure()
plt.hist(x,bins = d)
plt.show()

