import math
import numpy
import matplotlib.pyplot as plt
# import time

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def func(x):
    return math.exp(x) + x**2

def grad(x):
    return 2*x + math.exp(x)

def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

if __name__ == "__main__":
    a = -1
    b = 0
    h = 0.1
    e = 0.00000001
    eps = 0.000001
    g = 10

    x0 = a
    while True:
        g = grad(x0)
        i = sign(g)
        x = x0 - h*g
        g = grad(x)
        x0 = x
        i1 = sign(g)

        if math.fabs(g) < e:
            break
        else:
            if i != i1:
                h = h/2
            else: 
                h = 1.6 * h
                i = i1
        print('g = ',toFixed(g,6),'\ti = ',i,'\t i1 = ',i1,'\t x = ',toFixed(x,5))
        # time.sleep(0.2)
    
    X = numpy.linspace(a,b,100)
    Y = [func(i) for i in X]
    plt.plot(X,Y)
    plt.scatter(x,func(x))
    print(x,func(x),grad(x))
    plt.grid()
    plt.show()