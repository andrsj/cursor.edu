import matplotlib.pyplot as plt
import numpy as np


s = ['one','two','three ','four' ,'five']
x = [1, 2, 3, 4, 5]
z1 = [10, 17, 24, 16, 22]
z2 = [12, 14, 21, 13, 17]
z = np.random.random(100)

# bar()
fig = plt.figure()
plt.bar(x, z1)
plt.title('Simple bar chart')
plt.grid(True)   

# hist()
fig = plt.figure()
plt.hist(z1)
plt.title('Simple histogramm')
plt.grid(True)

# pie()
fig = plt.figure()
plt.pie(x, labels=s)
plt.title('Simple pie chart')

plt.show()
