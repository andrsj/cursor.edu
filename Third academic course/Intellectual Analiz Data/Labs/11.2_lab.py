import math
from matplotlib import pyplot as plt


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def Sum(x, w):
    s = 0
    for j in range(len(x)):
        s += w[j] * x[j]
    s += w[2]
    return s

def sigmoid(s):
    return 1 / (1 + math.exp(- (s)))


if __name__ == "__main__":
    w = []
    f = open("weight.txt","r")
    for line in f:
        w.append(float(line))
    print(w, " - ваги після навчання")
    x1 = [2,2.4]
    s = Sum(x1,w)
    out = sigmoid(s)
    print(out," - Вихід")

    koef = [- (w[0] / w[1]), - (w[2] / w[1])] # коефіцієнт прямої
    ax1.plot([1.0,4.0],[1.0 * koef[0] + koef[1],4.0 * koef[0] + koef[1]], color="blue")

    ax1.grid()
    ax1.scatter(x1[0],x1[1], c = "g" if out < 0.5 else "r")
    ax1.text(x1[0] + 0.01, x1[1] + 0.01, f"OUT:{out:3.4}")
    plt.show()
