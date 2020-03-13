import matplotlib.pyplot as plt
import math

# T(t) = (T0 - Ts) * e^(-rt) + Ts

t = [i * 0.1 for i in range(1000)]
r = 0.16
T0 = 82
Ts = 23
Ts_ = []
for i in t:
	Ts_.append(23)
T = []
for i in t:
	T.append(( (T0 - Ts) * math.exp(-r * i) + Ts ))


plt.figure()
plt.title("T(t) = (T0 - Ts) * e^(-rt) + Ts")
plt.xlabel("t секунда")
plt.ylabel("T температура")
plt.plot(t,T)
plt.plot(t,Ts_)
plt.grid()
plt.show()