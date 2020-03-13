import matplotlib.pyplot as plt


x = [2**(-32),]
# x = [0.00001,]

# M = [65700417,[0,0.002],400_000]
# M = [70041,[0,0.0002],2_000_000]
M = [417,[0,0.01],20_000]


while len(x) < M[2] * 2:
    x.append(M[0] * x[-1] - int(M[0] * x[-1]))
    # x.append((M[0] * x[-1]) % 1)




# plt.subplot(1,2,1)
# plt.plot(x[::2],x[1::2],".")
# plt.grid()

# plt.subplot(1,2,2)
plt.plot(x[::2],x[1::2],".")
plt.xlim(M[1])
plt.grid()

plt.suptitle("Метод лишків")
plt.show()