import numpy as np


x = np.arange(10)
print(x[2])

print(x[-2])

x.shape = (2,5) # now x is 2-dimensional
print(x[1,3])

print(x[1,-1])

print(x[0])

print(x[0][2])
print(x[0,2])






a = np.arange(12)**2                       # the first 12 square numbers
i = np.array( [ 1,1,3,8,5 ] )              # an array of indices
print(a[i])                                # the elements of a at the positions i
j = np.array( [ [ 3, 4], [ 9, 7 ] ] )      # a bidimensional array of indices
print(a[i])                                # the same shape as j


palette = np.array( [   [0,0,0],                # black
                        [255,0,0],              # red
                        [0,255,0],              # green
                        [0,0,255],              # blue
                        [255,255,255] ] )       # white
image = np.array( [ [ 0, 1, 2, 0 ],             # each value corresponds to a color in the palette
                    [ 0, 3, 4, 0 ]  ] )
print(palette[image])



a = np.arange(12).reshape(3,4)
print(a)

i = np.array( [ [0,1],     # indices for the first dim of a
                [1,2] ] )
j = np.array( [ [2,1],     # indices for the second dim of a
                [3,3] ] )

print(a[i,j])              # i and j must have equal shape

l = [i,j]
print(a[l])

print(a[i,2])






a = np.arange(5)
print(a)

a[[1,3,4]] = 0
print(a)
# array([0, 0, 2, 0, 0])



a = np.arange(5)
a[[0,0,2]]=[1,2,3]
print(a)
# array([2, 1, 3, 3, 4])


a = np.arange(5)
a[[0,0,2]]+=1
print(a)
# array([1, 1, 3, 3, 4])



a = np.arange(12).reshape(3,4)
b = a > 4
print(b)        # b is a boolean with a's shape
# array([[False, False, False, False],
#       [False,  True,  True,  True],
#       [ True,  True,  True,  True]])
print(a[b])     # 1d array with the selected elements
# array([ 5,  6,  7,  8,  9, 10, 11])


a[b] = 0        # All elements of 'a' higher than 4 become 0
print(a)
# array([[0, 1, 2, 3],
#        [4, 0, 0, 0],
#        [0, 0, 0, 0]])


a = np.arange(12).reshape(3,4)
b1 = np.array([False,True,True])             # first dim selection
b2 = np.array([True,False,True,False])       # second dim selection

a[b1,:]                                   # selecting rows
# array([[ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
a[b1]                                     # same thing
# array([[ 4,  5,  6,  7],
#       [ 8,  9, 10, 11]])

a[:,b2]                                   # selecting columns
# array([[ 0,  2],
#        [ 4,  6],
#        [ 8, 10]])
a[b1,b2]                                  # a weird thing to do
# array([ 4, 10])


c = np.arange(30)
c.shape = 2,-1 #!
print(c)