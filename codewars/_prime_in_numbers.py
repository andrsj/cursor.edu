def primeFactors(n):
    N = n
    for i in range(2,n-1):
        while not N % i:
            N /= 2
            print(N)


N = 7775460
print(N/2, N%2)
print(N/4, N%4)
print(N/8, N%8)
print("")
print(N/12, N%12)
print(N/36, N%36)
print(N/(2**2*3**3), N%(2**2*3**3))
print(N/(2**2*3**4), N%(2**2*3**4))



#"(2**2)(3**3)(5)(7)(11**2)(17)"
# print(primeFactors(7775460))
# 7775460