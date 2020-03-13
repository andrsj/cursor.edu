import numpy as np


z = np.linspace(2,10,5) #from 2 to 10, with 5 elements
# OUT: array( [ 2. , 4. , 6. , 8. , 10. ] )

np.random.seed(0)
z1 = np.random.randint(10, size = 6)
# OUT: array( [5, 0, 3, 3, 7, 9] )

z = np.array([1,2,3,4,5])
z < 3
# OUT: array([T,T,F,F,F])
z[z<3]
# OUT: array([1,2])

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

a + b  # - * /
# OUT: array([7,9,11,13,15])
a + 30 # - * /
# OUT: array([31,32,33,34,35])

a = np.array([[1,2,3],[4,5,6]])
print(a)
# OUT: [[1 2 3]
#       [4 5 6]]
a.shape()
# OUT: (2,3)
a.ndim()
# OUT: 2
a[0,2]
# OUT: 3
a[0,:]
# array([1,2,3])
a[:,1]
# array([2,4])

np.min(a) #or MAX|SUM
# OUT: 1



np.zeros(5)
# OUT: array([0.,0.,0.,0.,0.])
np.zeros_like([[10,10],[1,1]])
# OUT: [[0,0],[0,0]]
np.ones(3,2)
# OUT: array([[1,1],
#	    [1,1],
#	    [1,1]])
np.full((2,2),100)
# OUT: array([[100,100],
#	    [100,100]])
np.full_like((2,2), 10, dtype = np.int)
# OUT: [[10,10][10,10]]


np.random.rand(2,4)
#OUT: array([[x,x,x,x],
#	    [x,x,x,x]])

np.random.randint(10) 
#OUT: x # random from 0 to 10 (non include)

np.random.randint(5,10, size=(2,2)) #from 5 to 10(non include)
#OUT: array([[x,x],
#	    [x,x]])


a = [np.pi,-np.pi,0]
np.cos(a) 
#OUT: [-1,-1,1]


np.arange(10)
#OUT: [0,1,...,9]


v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

np.vstack([v1,v2,v1])

#1 2 3
#4 5 6
#1 2 3



a = np.array([1,2,3,4,5,6,7,8,9])
#a[[1,2,8]]
#OUT: 2,3,9


filedata = np.genfromtxt("name.txt", delimiter = ",")
# ?
filedata = filedata.astype("type") #!
# filedata[filedata > 50] 
# ((filedata > 50) & (filedata < 100))




# bool      Boolean (True or False) stored as a bit
# inti      Platform integer (normally either int32 or int64)
# int8      Byte (-128 to 127)
# int16     Integer (-32768 to 32767)
# int32     Integer (-2 ** 31 to 2 ** 31 -1)
# int64     Integer (-2 ** 63 to 2 ** 63 -1)
# uint8     Unsigned integer (0 to 255)
# uint16    Unsigned integer (0 to 65535)
# uint32    Unsigned integer (0 to 2 ** 32 - 1)
# uint64    Unsigned integer (0 to 2 ** 64 - 1)
# float16   Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
# float32   Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
# float64   Double precision float: sign bit, 11 bits exponent, 52 bits mantissa


a = np.arange(7, dtype='f')
# Integer                   i
# Unsigned integer          u
# Single precision float    f
# Double precision float    d
# Boolean                   b
# Complex                   D
# String                    S
# Unicode                   U
# Void                      V



x = np.arange(0,10,2)                       # x=([0,2,4,6,8])
y = np.arange(5)                            # y=([0,1,2,3,4])
m = np.vstack([x,y])                        # m=([[0,2,4,6,8],
                                            #     [0,1,2,3,4]])
xy = np.hstack([x,y])                       # xy =([0,2,4,6,8,0,1,2,3,4])