import matplotlib.pyplot as plt
import math

def display(X,Y,text):
    plt.figure()
    plt.suptitle(text)
    plt.plot(X,Y)
    plt.grid()
    plt.axvline(0)
    plt.axhline(0)

def Euler_Kromera(k,m,x,dT):
    t = 0
    v = 0
    w = math.sqrt(k/m)

    X = []
    T = []

    arrE = []
    arrEp = []
    arrEk = []
    V = []

    while t <= math.pi * 2 / w:
        X.append(x)
        T.append(t)
        V.append(v)

        v += (- w * w) * dT * x
        x += dT * v
        Ek = m * v**2 / 2
        Ep = k * x**2 / 2
        E = Ek + Ep
        t += dT

        arrE.append(E)
        arrEk.append(Ek)
        arrEp.append(Ep)


    display(T,X,"x(t)")
    display(T,arrE,"E(t)")
    display(T,arrEp,"Ep(t)")
    display(T,arrEk,"Ek(t)")
    display(X,V,"X(V)")

    plt.show()

def Euler(k,m,x,dT):
    t = 0
    v = 0
    w = math.sqrt(k/m)

    X = []
    T = []

    arrE = []
    arrEp = []
    arrEk = []
    V = []

    while t <= math.pi * 2 / w:
        X.append(x)
        T.append(t)
        V.append(v)

        x += dT * v
        v += (- w * w) * dT * x
        Ek = m * v**2 / 2
        Ep = k * x**2 / 2
        E = Ek + Ep
        t += dT

        arrE.append(E)
        arrEk.append(Ek)
        arrEp.append(Ep)


    display(T,X,"x(t)")
    display(T,arrE,"E(t)")
    display(T,arrEp,"Ep(t)")
    display(T,arrEk,"Ek(t)")
    display(X,V,"X(V)")


    plt.show()

if __name__ == "__main__":
    k = 2
    m = 0.125
    x = 2
    dT = 1/100
    Euler_Kromera(k,m,x,dT)
    Euler(k,m,x,dT)


# w = sqrt(k/m)
# T = 2pi / w
# 