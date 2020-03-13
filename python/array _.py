import array

a = array.array("i")

"""
'c' char
'b' signed char
'B' unsigned char
'u' symbol unicode
'h' short (16-bit number)
'H' unsigned short
'i' int
'I' unsigned int
'l' long
'L' unsigned long
'f' float
'd' double




a.typecode

a.append(x)

a.buffer_info() - Повертає кортеж (address, len) 
[адреса і розмір буферу в пам'яті, виділеного для збереженя масиву]

a.extend(b) - b - інший список / масив

a.fromlist(list)

a.index(x)

a.insert(i, x)

a.pop([i])

a.remove(x)

a.reverse()

a.tolist()

a = array.array(“i”, [1,2,3,4,5])
b = array.array(a.typecode, (2*x for x in a))

a = array.array(“i”, [1,2,3,4,5])
    for i, x in enumerate(a):
        a[i] = 2*x


"""