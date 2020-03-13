def namelist(names):
    s = ""
    for i in names[:-2]:
        for key in i:
            s += f"{i[key]}, "
    for i in names[-2:]:
        for key in i:
            s += f"{i[key]} & "
    return s[:-2]


def namelist1(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''

def namelist2(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']

def namelist3(names):
    return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]

def namelist4(names):
    nameList = [elem['name'] for elem in names]
    return ' & '.join(', '.join(nameList).rsplit(', ', 1))

def namelist4_(names):
    return ' & '.join(', '.join([elem['name'] for elem in names]).rsplit(', ', 1))

a = [ {"name" : "LOL"} ]
b = [ {"name" : "LOL"} , {"name" : "KEK"} ]
c = [ {"name" : "LOL"} , {"name" : "KEK"}, {"name" : "LUL"} ]
d = [ {"name" : "LOL"} , {"name" : "KEK"}, {"name" : "LUL"}, {"name" : "KOK"} ]

print(namelist(a))
print(namelist(b))
print(namelist(c))
print(namelist4_(d))