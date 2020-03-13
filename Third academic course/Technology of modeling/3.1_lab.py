import math
import matplotlib.pyplot as plt

def calculated(h,a,dT):
    T = 0
    V = 0
    y = 0
    arrT = []
    arrH = []
    arrV = []

    while True:
        arrT.append(T)
        arrV.append(V)
        arrH.append(h-y)

        if y >= h:
            break

        T += dT
        V += a*dT
        y += dT * V

    plt.figure()
    plt.suptitle("Обрахунковий")

    plt.subplot(121)
    plt.plot(arrT,arrH)
    plt.grid()
    plt.axvline(0)
    plt.axhline(0)

    plt.subplot(122)
    plt.plot(arrT,arrV)
    plt.grid()
    plt.axvline(0)
    plt.axhline(0)


    print("Обрахунковий:")
    print("T = ",arrT[-1],"\t V = ",arrV[-1])
    # print("sqrt ( 2h / g) = ", math.sqrt(2*h/a))


def Euler(h,a,dT):
    arrT = []
    arrH = []
    arrV = []
    T = 0
    V = 0
    y = h

    while True:
        arrT.append(T)
        arrV.append(V)
        arrH.append(y)

        if y <= 0:
            break

        T = T + dT
        y = y - dT * V
        V = V + dT * a


    plt.figure()
    plt.suptitle("Ейлера")
    plt.subplot(121)
    plt.plot(arrT,arrH)
    plt.grid()
    plt.axvline(0)
    plt.axhline(0)

    plt.subplot(122)
    plt.plot(arrT,arrV)
    plt.grid()
    plt.axvline(0)
    plt.axhline(0)

    print("Ейлера:")
    print("T = ",arrT[-1],"\t V = ",arrV[-1], arrH[-1])


def Euler_Kramer(h,a,dT):
    y = h
    V = 0
    arrH = []
    arrV = []

    while True:
        arrH.append(y)
        arrV.append(V)

        if y <= 0:
            break

        V = V + dT * a
        y = y - dT * V


    arrT = []
    for i in arrH:
        arrT.append(arrH.index(i) * dT)

    plt.figure()
    plt.suptitle("Ейлера - Крамера")

    plt.subplot(121)
    plt.plot(arrT,arrH)
    plt.grid()
    plt.axvline(0)
    plt.axhline(0)
    
    plt.subplot(122)
    plt.plot(arrT,arrV)
    plt.grid()
    plt.axvline(0)
    plt.axhline(0)

    print("Ейлера - Крамера:")
    print("T = ",len(arrH) * dT,"\t V = ",V)


if __name__ == "__main__":
    h = 2.9
    a = 9.8
    dT = 1/1000
    calculated(h,a,dT)
    Euler(h,a,dT)
    Euler_Kramer(h,a,dT)
    plt.show()