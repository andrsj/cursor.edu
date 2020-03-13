def find_uniq1(arr):
    return [i for i in set(arr) if arr.count(i) == 1][0]

def find_uniq2(arr):
    i = set(arr)
    for j in i:
        if arr.count(j) == 1:
            return j

def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b