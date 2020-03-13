import numpy as np


a = np.arange(5)
print(a,a.dtype,a.shape, "arange(5) A")
# print(np.finfo(np.float16))
print(np.arange(7, dtype = np.uint8), "arange(7) uint8")
print(np.arange(7, dtype = np.float), "arange(7) float")
b = np.arange(24, dtype = "f").reshape(6,4)
print(b, "arange(24) float (6,4) B")
# print(b.ravel())                  #! in 1D array
print(b.flatten() , "B 1D-array")   #! in 1D array

# np.array.ravel () Эта функция возвращает одномерный массив с теми же данными, что и входной массив и не всегда возвращает копию 
# np.array.flatten () Это метод ndarray, который выравнивает массивы и всегда возвращает копию массива
# np.array.reshape (x,y) Эта функция изменяет форму массива
# np.array.resize ((x,y)) Эта функция меняет форму массива и при необходимости добавляет копии входного массива

b.shape = (4,6)
print(b,"arange(24) (4,6) B")
b = b.transpose() # b.T
print(b,"transpose B")
b.resize((2,12))
print(b,"arange(24) (2,12) B")

c,d = np.arange(3),np.arange(3)
print(c == d, "c == d")

f = np.arange(6, dtype = "f").reshape(2,3)
print(f, "arange(6) (2,3) F")
hf = np.hsplit(f,3)
print("hsplit:")
for i in hf:
    print(i)
vf = np.vsplit(f,2)
print("vsplit:")
print(vf)
print()
print("ndim","size","itemsize","nbytes")
print(b.ndim,b.size,b.itemsize,b.nbytes)

print(b.flat[3],"b.flat -> 3 index element of B") 
b.flat = 1
print(b, "B after b.flat = 1")
b.flat[[6,10]] = 4
print(b, "B after b.flat[[6,10]] = 4")

b = b.tolist()
print(b,"\n B - list python")

print(a, np.mean(a) , "A and A-means")
print(np.max(a), np.min(a) , "max and min")
print(np.median(a), "Median of A")
print(np.sign(a), "+- of A")

k = np.full_like(a, 10, dtype = np.int)
print(k, 'Full like A by 10s in K')

A = np.mat('1 2 -3.0; -4.1 5.1 6.1; 0.1 0 9')
print(A, "A from string")
A = np.eye(3)
print(A, "Діагональна матриця")
B = A * 2
print(np.bmat("A B; B A"), "Compound matrix")



a = np.array([2, 6, 5])
b = np.array([1, 2, 3])
print(np.divide(a, b), np.divide(b, a), "Divide")
print(np.true_divide(a, b), np.true_divide(b, a), "True Divide")


a = np.array([[1, 2], [3, 4]], int)
b = np.array([[5, 6], [7,8]], int)
c = np.concatenate((a,b))
print(c)

print(np.arange( 0, 2, 0.3 ), "arange float!")


A = np.array( [[1,1],[0,1]] )
B = np.array( [[2,0],[3,4]] )
print(A * B, "По одиночне множення")
print(A @ B, "Множення матриць") # A.dot(B)


def func(x,y):
    return 10*x+y

b = np.fromfunction(func,(5,4),dtype=int)
print(b)


a = np.floor(10 * np.random.random((3,4)))
print(a)


z = np.arange(3, dtype=np.uint8)
print(z, "Z")
print(z.astype(float), "Z float")
np.int8(z)
print(z,z.dtype, "Z")