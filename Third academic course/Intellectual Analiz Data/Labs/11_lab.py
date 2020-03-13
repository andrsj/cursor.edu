import math
import random
from matplotlib import pyplot as plt


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def gen_vec(x,y):
    a = []
    b = []
    # Генеруємо по десять векторів з кожного класу
    for i in range(10):
        a.append([x[0] + random.random(), y[0] + random.random()])
        b.append([x[1] + random.random(), y[1] + random.random()])
    return a, b

def Sum(x, w):
    s = 0
    for j in range(len(x)):
        s += w[j] * x[j]
    s += w[2]
    return s

def sigmoid(s):
    return 1 / (1 + math.exp(- (s)))

# Похідна сигмоїдальна функція активації
def sigmoid_dx(s):
    return math.exp(- (s)) / ((1 + math.exp(- (s))) ** 2)

def eps(t, out):
    return 0.5 * (out - t)**2

def delta(t, out, s):
    return (out - t) * sigmoid_dx(s)

# Навчання
def iter_f(i, t, arr, w):
    s = Sum(arr[i], w)
    out = sigmoid(s)
    e = eps(t, out)

    if e <= e_:
        return 0

    d = delta(t, out, s)
    w[0] -= n * d * arr[i][0]
    w[1] -= n * d * arr[i][1]
    w[2] -= n * d
    return 1

if __name__ == "__main__":
    A, B = gen_vec([1,3],[1,3])
    w = [random.random(), random.random(), random.random()]
    print(w," - Ваги перед навчанням")
    e_ = 0.1
    n = 0.7
    OUTA = 0
    OUTB = 1
    
    kilk = 0
    while True:
        for i in range(10):
            kilk += iter_f(i, OUTA, A, w)
            kilk += iter_f(i, OUTB, B, w)
        if kilk == 0:
            break
        kilk = 0

    #Графічний вивід
    koef = [- (w[0] / w[1]), - (w[2] / w[1])] # коефіцієнт прямої
    ax1.plot([1.0,4.0],[1.0 * koef[0] + koef[1],4.0 * koef[0] + koef[1]], color="blue")

    for i in range(10):
        ax1.scatter(A[i][0], A[i][1], color="green")
        ax1.scatter(B[i][0], B[i][1], color="red")

    ax1.grid()
    ax1.axvline(0)
    ax1.axhline(0)
    print(w," - ваги після навчання")
    f = open("weight.txt","w")
    for i in w:
        f.write(str(i) + '\n')
    f.close()
    plt.show()