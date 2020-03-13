def dig_pow(n,p):
    b = []
    N = n
    while N > 0:
        b.append(N % 10)
        N = N // 10
    b = b[::-1]
    sum = 0
    for i in b:
        sum += i**p
        p += 1
    return int(sum/n) if sum//n else -1

print(dig_pow(89, 1), 1)
print(dig_pow(92, 1), -1)
print(dig_pow(46288, 3), 51)