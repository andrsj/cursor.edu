import matplotlib.pyplot as plt

def model(E,R,C,dt,text):

    t = 0
    u = 0

    T = [t]
    U = [u]
    I = [ (E - u) / R ]



    while t < 0.0035:
        t += dt
        u += dt * ((E-u)/(R*C))
        i = (E - u) / R

        T.append(t)
        U.append(u)
        I.append(i)

    plt.figure()
    plt.suptitle(text)

    plt.subplot(211)
    plt.plot(T,U)
    plt.ylabel("U")
    plt.grid()

    plt.subplot(212)
    plt.plot(T,I)
    plt.ylabel("I")
    plt.grid()

    plt.show()


if __name__ == "__main__":
    E = 14
    R = 2500
    C = 180.0e-9
    dt = 1e-3 * R * C

    model(E,R,C,dt,"0.001 * R * C")