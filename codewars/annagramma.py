def anagrams(word, words):
    a = []
    for i in words:
        if len(word) == len(i) and set(word) == set(i):
            a.append(i)
    return a

def anagrams_GENIUS_MY(word, words):
    return [i for i in words if len(word) == len(i) and set(word) == set(i)]

def anagrams_GENIUS_1(word, words): return [item for item in words if sorted(item)==sorted(word)]

def anagrams_GENIUS_2(word, words):
    return filter(lambda x: sorted(word) == sorted(x), words)

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))