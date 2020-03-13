import math
import matplotlib.pyplot as plt

def calculated(h,a,dT,m,k,kv):
    T = 0
    V = 0
    y = 0
    arrT = []
    arrH = []
    arrV = []

    while y < h:
        arrT.append(T)
        arrV.append(V)
        arrH.append(h-y)
        T += dT
        if kv:
            A = a - k * V**2 / m
        else:
            A = a - k * V / m
        V += A*dT
        y += V*dT + A*dT**2/2

    plt.figure()
    plt.suptitle("Обрахунковий")

    plt.subplot(121)
    plt.plot(arrT,arrH)
    plt.grid()
    plt.axvline(0)
    plt.axhline(0)

    plt.subplot(122)
    plt.plot(arrT,arrV)
    if not kv:
        plt.plot(arrT,[m*a/k] * len(arrT))
    else:
        plt.plot(arrT,[math.sqrt(m*a/k)] * len(arrT))
    plt.grid()
    plt.axvline(0)
    plt.axhline(0)


    print("Обрахунковий:")
    print("T = ",T,"\t V = ",V)


def Euler(h,a,dT,m,k,kv):
    arrT = []
    arrH = []
    arrV = []
    T = 0
    V = 0
    y = h

    while y > 0:
        arrT.append(T)
        arrV.append(V)
        arrH.append(y)
        T += dT
        if kv:
            A = a - k * V**2 / m
        else:
            A = a - k * V / m
        y = y - dT * V
        V = V + dT * A

    plt.figure()
    plt.suptitle("Ейлера")
    plt.subplot(121)
    plt.plot(arrT,arrH)
    plt.grid()
    plt.axvline(0)
    plt.axhline(0)

    plt.subplot(122)
    plt.plot(arrT,arrV)
    if not kv:
        plt.plot(arrT,[m*a/k] * len(arrT))
    else:
        plt.plot(arrT,[math.sqrt(m*a/k)] * len(arrT))
    plt.grid()
    plt.axvline(0)
    plt.axhline(0)

    print("Ейлера:")
    print("T = ",T,"\t V = ",V)


def Euler_Kramer(h,a,dT,m,k,kv):
    y = h
    V = 0
    arrH = []
    arrV = []

    while y > 0:
        arrH.append(y)
        arrV.append(V)
        if kv:
            A = a - k * V**2 / m
        else:
            A = a - k * V / m
        V += dT * A
        y -= dT * V

    plt.figure()
    plt.suptitle("Ейлера - Крамера")

    arrT = []
    for i in arrH:
        arrT.append(arrH.index(i) * dT)

    plt.subplot(121)
    plt.plot(arrT,arrH)
    plt.grid()
    plt.axvline(0)
    plt.axhline(0)
    
    plt.subplot(122)
    plt.plot(arrT,arrV)
    if not kv:
        plt.plot(arrT,[m*a/k] * len(arrT))
    else:
        plt.plot(arrT,[math.sqrt(m*a/k)] * len(arrT))
    plt.grid()
    plt.axvline(0)
    plt.axhline(0)

    print("Ейлера - Крамера:")
    print("T = ",len(arrH) * dT,"\t V = ",V)


if __name__ == "__main__":
    h = 2.9
    a = 9.8
    k = 0.8
    m = 0.115
    dT = 1/100
    kv = False
    
    if kv:
        print("Максимальна швидкість:", math.sqrt(m * a / k))
    else:
        print("Максимальна швидкість:", m * a / k)

    calculated(h,a,dT,m,k,kv)
    Euler(h,a,dT,m,k,kv)
    Euler_Kramer(h,a,dT,m,k,kv)
    plt.show()