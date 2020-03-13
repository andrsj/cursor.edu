def romSum(a: str, b: str) -> str:
    return fromArabToRom(fromRomToArab(a) + fromRomToArab(b))

# d = {
#     'M': 1000,
#     'D': 500,
#     'C': 100,
#     'L': 50,
#     'X': 10,
#     'V': 5,
#     'I': 1,
# }

d = {
    'M':  1000,
    'CM': 900,
    'D':  500,
    'CD': 400,
    'C':  100,
    'XC': 90,
    'L':  50,
    'XL': 40,
    'X':  10,
    'IX': 9,
    'V':  5,
    'IV': 4,
    'I':  1,
}

def fromRomToArab(number:str) -> int:
    num, cache = 0, 0
    for i,j in zip(number[:-1],number[1:]):
        if d[i] >= d[j]: num += d[i]
        else: cache += d[i]
    return num + d[number[-1]] - cache

def fromArabToRom(number:int) -> str:
    result = ''
    for i in d:
        while number >= d[i]:
            number -= d[i]
            result += i
    return result

if __name__ == '__main__':
    print(romSum('XLIX','X'))
    print(romSum(fromArabToRom(1001),fromArabToRom(2061)))