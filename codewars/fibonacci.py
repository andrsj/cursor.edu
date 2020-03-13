# 0 1 1 2 3 5  8  13  21  34  55   89   144   233
#   0 1 2 6 15 40 104 273 714 1870 4895 12816 33552

def fibonacci(n):
    a = [0,1]
    for i in range(n):
        a.append(a[-2] + a[-1])
    return (a[-1],a[-1]*a[-2])

def productFib_(p):
    i = 0
    while p > fibonacci(i)[1]:
        i += 1
    return [fibonacci(i-1)[0],fibonacci(i)[0],True if p == fibonacci(i)[1] else False]


def productFib_GENIUS(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]

