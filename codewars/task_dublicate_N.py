def delete_nth(order,max_e):
    b = []
    c = {i:1 for i in order}
    for i in order:
        if c[i] <= max_e:
            b.append(i)
            c[i] += 1
    return b

def delete_nth1(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans

def delete_nth2(order,max_e):
    return [o for i,o in enumerate(order) if order[:i].count(o)<max_e ] #! yes

print(delete_nth([20,37,20,21], 1), [20,37,21])
print(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])