import matplotlib.pyplot as plt


# m = [65700417,[0,0.002],400_000]
# m = [70041,[0,0.0002],2_000_000]
m = [417,[0,0.01],20_000]

def generator():
    x = 2**(-32)
    while True:
        x = (m[0] * x) % 1
        yield x

gen = generator()
arr = [next(gen) for i in range(m[2] * 2)]



# plt.subplot(1,2,1)
# plt.plot(arr[::2],arr[1::2],".")
# plt.grid()

# plt.subplot(1,2,2)
plt.plot(arr[::2],arr[1::2],".")
plt.xlim(m[1])
plt.grid()

plt.suptitle("Метод лишків")
plt.show()