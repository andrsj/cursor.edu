def unique_in_order(iterable):
    a = [iterable[0]] if iterable else []
    for i in iterable:
        if a[-1] != i:
            a.append(i)
    return a

def unique_in_order1(iterable):
    r = []
    for x in iterable:
        x in r[-1:] or r.append(x)
    return r

def unique_in_order2(it):
    return [it[0]] + [e for i, e in enumerate(it[1:]) if it[i] != e] if it else []

def unique_in_order3(iterable):
    return [ ch for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1] ]

def unique_in_order4(sequence):
    return [sequence[i] for i in range(len(sequence)) if not i or sequence[i] != sequence[i-1]]

def unique_in_order5(iterable): return (lambda y: [j for i,j in enumerate(y) if i==0 or j!=y[i-1]])(list(iterable))

print(unique_in_order("AAAABBBCCDAABBB"))
print([ch + " " + str(i) for i,ch in enumerate("AAAABBBCCDAABBB")])