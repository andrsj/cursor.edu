from io import StringIO   # StringIO behaves like a file object
import numpy as np
c = StringIO(u"1,0,2\n3,0,4")
x, y = np.loadtxt(c, delimiter=',', usecols=(0, 2), unpack=True)
# x, y = np.loadtxt(c, delimiter=',', usecols=(0, -1), unpack=True)
print(x,y)


data = u"""#
# Skip me !
# Skip me too !
1, 2
3, 4
5, 6 #This is the third line of the data
7, 8
# And here comes the last line
9, 0
"""
print(np.genfromtxt(StringIO(data), comments="#", delimiter=","))



data = u"\n".join(str(i) for i in range(10))
print(np.genfromtxt(StringIO(data)), "without skipping")
print(np.genfromtxt(StringIO(data),skip_header=3, skip_footer=5), "with skipping")




data = StringIO("1 2 3\n 4 5 6")
print(np.genfromtxt(data, dtype=(int, float, int))) #! Types
