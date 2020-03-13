import numpy
import matplotlib.pyplot as plt
import random as rand

def Sum(x,w):
    sum = 0
    for i,j in zip(x,w):
        sum += i*j
    return sum

def OUT(alpha,S):
    return 1 / (1 + numpy.exp(-alpha * S))

def grad(out,T,x):
    return (out - T) * out * (1 - out) * x

def weight(n,w,out,T,x):
    return w - n * grad(out,T,x)

if __name__ == "__main__":
    alpha = 0.4
    E = 10
    E_ = 0.01
    n = 0.7
    OUT_end = 0

    x1,x2 = 1,1
    x = [x1, x2, 1]
    print(x, "\t - x")
    w = [rand.random(),rand.random(),rand.random()]
    print(w, "\t - w")

    while True:
        S = Sum(x,w)
        print(S, "\t - S")
        Out = OUT(alpha,S)
        print(Out, "\t - Out")
        E = 1/2 * (Out - OUT_end) ** 2

        if E < E_:
            break
        
        w[0] = w[0] - n * ((Out - OUT_end) * Out * (1 - Out) * x[0])
        w[1] = w[1] - n * ((Out - OUT_end) * Out * (1 - Out) * x[1])
        w[2] = w[2] - n * ((Out - OUT_end) * Out * (1 - Out) * x[2])

        print(w, "\t - w")

    plt.scatter(S,Out)
    X = numpy.linspace(-10,10,200)
    Y = Y = [OUT(alpha,i) for i in X]
    plt.plot(X,Y)

    x = [1 + rand.random(),1 + rand.random(),0]


    S = Sum(x,w)
    print(S, "\t - S")
    Out = OUT(alpha,S)
    print(Out, "\t - Out")

    plt.scatter(S,Out)


    x = [3 + rand.random(),3 + rand.random(),1]


    S = Sum(x,w)
    print(S, "\t - S")
    Out = OUT(alpha,S)
    print(Out, "\t - Out")

    plt.scatter(S,Out)
    plt.text(S + 0.01, Out + 0.01, "3,3,1")



    plt.grid()
    plt.axvline(0)
    plt.axhline(0)
    plt.show()

# E = 0,01
# 0,47 0,89 0,52        3|3|1
# -1,53 -1,06 -1,92     1|1|0

# E = 0,1
# rand rand rand        3|3|1
# 0,21 -0,21 -0,57      1|1|0