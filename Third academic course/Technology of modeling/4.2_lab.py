import matplotlib.pyplot as plt
import math

def display(X,Y,text):
    # plt.figure()
    plt.suptitle(text)
    plt.plot(X,Y)
    plt.grid()
    plt.axvline(0,linewidth = 0.5)
    plt.axhline(0,linewidth = 0.5)

def Euler_Kromera(k,m,x,dT,r):
    t = 0
    v = 0
    w = math.sqrt(k/m)

    X = []
    T = []

    arrE = []
    arrEp = []
    arrEk = []
    V = []

    while len(X) <= 2000:
        X.append(x)
        T.append(t)
        V.append(v)

        v += - dT * (x * w**2 + (r/m) * v)
        x += dT * v
        Ek = m * v**2 / 2
        Ep = k * x**2 / 2
        E = Ek + Ep
        t += dT

        arrE.append(E)
        arrEk.append(Ek)
        arrEp.append(Ep)


    display(T,X,"x(t)")
    # display(T,arrE,"E(t)")
    # display(T,arrEp,"Ep(t)")
    # display(T,arrEk,"Ek(t)")
    # display(X,V,"X(V)")


    # plt.show()

def Euler(k,m,x,dT,r):
    t = 0
    v = 0
    w = math.sqrt(k/m)

    X = []
    T = []

    arrE = []
    arrEp = []
    arrEk = []
    V = []

    while len(X) <= 2000:
        X.append(x)
        T.append(t)
        V.append(v)

        x += dT * v
        v += - dT * (x * w**2 + (r/m) * v)
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
    k = 1
    m = 1
    r = [0.5,2,10]
    x = 1
    dT = 1/100
    Euler_Kromera(k,m,x,dT,r[0])
    Euler_Kromera(k,m,x,dT,r[1])
    Euler_Kromera(k,m,x,dT,r[2])
    # Euler(k,m,x,dT,r[0])
    # Euler(k,m,x,dT,r[1])
    # Euler(k,m,x,dT,r[2])
    plt.show()


# d2x / dt2 + 2Y dx/dt + w0^2 * x = 0
# y^2 < w0 ^2 
# y^2 = w0 ^2
# y^2 > w0 ^2