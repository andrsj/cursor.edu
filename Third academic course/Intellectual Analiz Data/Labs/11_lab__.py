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

def Neuron(x1,x2):
    x = [x1 + rand.random(), x2 + rand.random() , 1]
    print(x)
    w = [rand.random(),rand.random(),rand.random()]
    print(w)
    S = Sum(x,w)
    print(S)
    Out = OUT(0.3,S)
    return Out

if __name__ == "__main__":
    output = []
    # print(output)
    for i in range(10):
        output.append(Neuron(1,1))
    for i in range(10):
        output.append(Neuron(3,3))

    print(output)
    print(sorted(output))
    plt.plot(sorted(output))
    plt.show()