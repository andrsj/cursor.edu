import math
import numpy
import matplotlib.pyplot as plt
# import time

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def func(x):
    return math.exp(x) + x**2
    # return (x+2)/x**2 - x

def grad(x):
    return 2*x + math.exp(x)

def grad1(x,x0):
    return (func(x0 + eps) - func(x)) / eps

def grad2(x,x0):
    return (func(x) - func(x0)) / (x - x0)

def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

if __name__ == "__main__":
    a = -1
    b = -0
    h = 0.1
    e = 1e-4   # min 1e-8
    eps = 1e-5 # min 1e-9
    g = 10

    x0 = a
    x = a
    count = 0
    while True:
        g = grad1(x,x0)
        i = sign(g)
        x = x0 - h*g
        # print(g,i,x,x0,h)
        g = grad2(x,x0)
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
        count += 1
        # print('g = ',toFixed(g,6),'\ti = ',i,'\t i1 = ',i1,'\t x = ',toFixed(x,5))
        # time.sleep(0.2)
    
    X = numpy.linspace(a,b,100)
    Y = [func(i) for i in X]
    plt.plot(X,Y)
    plt.scatter(x,func(x))
    print("[",a,':',b,"]\t x = ",x,"\t f(x) = ",func(x),"f`(x) = ",grad(x), "\t Iter = ",count , "\t eps = ", eps, "\te = ",e)
    plt.grid()
    plt.show()