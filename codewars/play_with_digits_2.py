def sum_dig_pow1(a, b):
    return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]

def sum_dig_pow(a, b):
    arr = []
    for i in range(a,b + 1):
        sum = 0
        k = 1
        for j in list(str(i)):
            sum += int(j)**k
            k += 1
        if sum == i:
            arr.append(i)
    return arr


print(sum_dig_pow(1,10),[i for i in range(1,10)])
print(sum_dig_pow(1,100),[i for i in range(1,10)] + [89])
print(sum_dig_pow(10,89),[89])
print(sum_dig_pow(10,100),[89])
print(sum_dig_pow(90,100),[])

