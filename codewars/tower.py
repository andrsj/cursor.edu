def tower_builder(n):
    a = []
    for i in range(n):
        a.append(" "*i + "*"*(2*n - 2*i - 1) + " "*i)
    a.reverse()
    return a