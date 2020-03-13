import random as rand
from collections import Counter
import matplotlib.pyplot as plt
x = []
i = 0
while i < 1000:
    x.append(rand.randint(100,1000))
    i += 1
Mx = sum(x)/len(x)
# print(Mx)
Dx = sum(i*i for i in x)/len(x) - Mx**2
# print(Dx)

count_items = Counter(x)
# print(count_items)

count_items_sort_keys = list(count_items.keys())
count_items_sort_keys.sort()

# Сортування ключів словника
# for i in count_items_sort_keys:
#    print(i, ":", count_items[i])

# Вивід пари ключ-значення рандомного числа
# z = rand.randint(100,1000)
# print(count_items[z],z)

# for i in count_items_sort_keys:
#     print (i, ":", count_items[i])
#     if i >= 120:
#         break


# a = [102,102,103,103,104,104,105,105,106,106]
# b = [0,2,2,3,3,4,4,5,5,7]

# plt.plot(a,b)
# plt.grid()
# plt.show()


# List of OX points
a = []
OX = []
for i in count_items_sort_keys:
    a.append(i)
for i in a:
    OX.extend([i, i])
# print(OX)




b = []
OY = [0,]
for i in count_items_sort_keys:
#     print(i, ":", count_items[i])
    b.append(count_items[i])
#     if i >= 120: 
#         break

# print(b)
k = 1
c = []
while k <= len(b):
#     print(b[:k])
    c.append(sum(b[:k]))
    k += 1
# print(c)

for i in c:
    OY.extend([i, i])
OY.pop()
# print(OY)



print(len(OY),"\t",len(OX))


plt.plot(OX,OY)
plt.grid()
plt.show()

plt.hist(x,bins = 1000)
plt.show()