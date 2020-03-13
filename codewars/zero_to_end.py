a = ["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]

def move_zeros_1_(array):
    for i in array:
        # print(i, i == 0, i is 0)
        if i is 0:
            array.remove(0)
            array.append(0)
    return array

def move_zeros_2_(array):
    return [i for i in array if i is not 0] + [i for i in array if i is 0]

def move_zeros_3_(array):
    array.sort(key=lambda item: item is 0)
    return array

def move_zeros_3(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)

def move_zeros_4(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)

def move_zeros_GENIUS(array):
    return [i for i in array if i is not 0 and type(i) != float] + [i for i in array if i == 0 and type(i) != bool]

print(0.0 is 0)
print(type(False) == bool)