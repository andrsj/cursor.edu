def spin_words_my(sentence):
    sentence = [list(i) for i in sentence.split(" ")]
    for i in sentence:
        if len(i) >= 5:
            i.reverse()
    sentence = ["".join(i) for i in sentence]
    return " ".join(sentence)


def spin_words1(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

def spin_words2(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)

def spin_words3_my(sentence):
    return " ".join(["".join(i) if len(i)<=4 else "".join(reversed(i)) for i in reversed(sentence.split(" "))])


print(spin_words3_my("Welcome"))
print(spin_words3_my("Welcome test"))
print(spin_words3_my("Test"))