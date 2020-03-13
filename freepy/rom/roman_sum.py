def romSum(a: str, b: str) -> str:
    """
    Write method to add two roman numbers.
    Use Old Roman style
    1 - I
    2 - II
    3 - III
    4 - IIII
    5 - V
    6 - VI
    7 - VII
    8 - VIII
    9 - VIIII
    10 - X
    ...
    result = roman_sum('II', 'II')
    print(result)
    >>>> IIII
    """
    return fromArabToRom(fromRomToArab(a) + fromRomToArab(b))

def fromRomToArab(number:str) -> int:
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
        'XI': 9,
        'V':  5,
        'IV': 4,
        'I':  1,
    }
    for i in number:
        if i not in d: return
    num = 0
    cache = 0
    for i,j in zip(number[:-1],number[1:]):
        if d[i] >= d[j]: num += d[i]
        else: cache += d[i]
    return num + d[number[-1]] - cache

def fromArabToRom(number:int) -> str:
    result = ''
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
        'XI': 9,
        'V':  5,
        'IV': 4,
        'I':  1,
    }
    for i in d:
        while number >= d[i]:
            number -= d[i]
            result += i
    return result

def roman(number: int) -> str:
    result = ''
    for i in d:
        while number >= d[i]:
            print("До {} -> {}".format(number,number%d[i]))
            number -= d[i]
            print("Після {}\n".format(number))
            result += i
    return result

def r(x:int) -> str:
    while x:
        print(x, x%10)
        x //= 10
        print(x, x%10, '\n')


d = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
}

if __name__ == '__main__':
    # print(romSum('XLIX','X'))
    print(romSum(fromArabToRom(1001),fromArabToRom(2061)))
    # print(fromArabToRom(194))
    # print(fromRomToArab('CXCIV'))
    # print(roman(194))


    # numbers = [ 'I',    'II',   'III',  'IV',   'V',    'VI',   'VII',  'VIII',  'IX',  'X',
    #             'XI',   'XII',  'XIII', 'XIV',  'XV',   'XVI',  'XVII', 'XVIII', 'XIX', 'XX',
    #             'XXI',  'XXII', 'XXIII','XXIV', 'XXV',  'XXVI', 'XXVII','XXVIII','XXIX','XXX'
    #         ]
    # for i,j in enumerate(numbers, start = 1):
    #     print(fromArabToRom(i) == j, i, j)


    # numbers = [ 'I',    'II',   'III',  'IV',    'V',    'VI',   'VII',   'VIII',   'IX',   'X',
    #             'XI',   'XII',  'XIII', 'XIV',   'XV',   'XVI',  'XVII',  'XVIII',  'XIX',  'XX',
    #             'XXI',  'XXII', 'XXIII','XXIV',  'XXV',  'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX',
    #             'XXXI', 'XXXII','XXXIII','XXXIV','XXXV', 'XXXVI','XXXVII','XXXVIII','XXXIX','XXXX'
    #         ]
    # for i,j in enumerate(numbers, start = 1):
    #     print(fromRomToArab(j) == i , j, i)


    # from roman import toRoman
    # numbers = [toRoman(i) for i in range(1,2005)]
    # for i,j in enumerate(numbers, start = 1):
    #     print(fromRomToArab(j) == i , j, i)


'''
IVX -> 1 + 5 + 10
VIX -> 5 - 1 + 10


20 -> X X
16 -> X V I
14 -> X I V
12 -> X I I
8  -> V I I I
6  -> V I
4  -> I V
'''