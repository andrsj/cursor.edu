import math
import matplotlib.pyplot as plt

eps = 1e-5
e = eps * 3
a = -1
b = 0

def func(x):
    return math.exp(x) + x**2

x = a
N = 100
h = math.fabs(a - b) / N
X = []
for i in range(N):
    X.append(x)
    x += h

Y = []
for i in X:
    Y.append(func(i))

i = 0
while math.fabs(b - a) > e:
    p = (a+b)/2 + eps
    q = (a+b)/2 - eps
    if func(p) < func(q):
        a = q
    else:
        b = p
    i += 1

x = (a+b) / 2

plt.scatter(x,func(x))
print("[",-1,':',0,']\t x = ',x,'\t f(x) = ',func(x), '\t eps = ', eps, '\t Iter = ',i)
plt.text(x + 0.01, func(x) + 0.01, "Min")
plt.plot(X,Y)
plt.grid()
plt.show()