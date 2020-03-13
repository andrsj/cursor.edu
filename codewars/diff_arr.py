def array_diff1(a: list, b: list):
    return [x for x in a if x not in b]

def array_diff2(a, b):
    return [x for x in a if x not in set(b)]

def array_diff3(a, b):
    return filter(lambda i: i not in b, a)

def array_diff4(a, b):
    for n in b:
        while(n in a):
            a.remove(n)
    return a

def array_diff5(a, b):
    for el in b:
        while el in a:
            a.remove(el)
        return a

