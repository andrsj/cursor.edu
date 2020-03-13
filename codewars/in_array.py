# print("arp" in "harp")
# print("live" in "lively")
# print("live" in "Lively")
# print("Live" in "lively")

def in_array(a1, a2):
    a = []
    for i in a1:
        for j in a2:
            if i in j:
                a.append(i)
    a = set(a)
    return sorted(list(a))

def in_array_my_final(a1,a2):
    return sorted(list(set([i for i in a1 for j in a2 if i in j])))


def in_array_my_final_final(a1,a2):
    return sorted((set([i for i in a1 for j in a2 if i in j])))

def in_array2(a1, a2):
    a = []
    for i in a1:
        for j in a2:
            if i in j:
                a.append(i)
    a.sort()
    return list(set(a))

def in_array3(a1, a2):
    return sorted({w for w in a1 if w in "".join(a2)})

a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']
print(in_array_my_final_final(a1,a2))