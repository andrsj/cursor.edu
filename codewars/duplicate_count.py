def duplicate_count1(text):
    text = text.lower()
    count = 0
    for i in set(text):
        if text.count(i) > 1:
            count += 1
    return count


def duplicate_count2(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])

def duplicate_count3(text):
    text = text.lower()
    return(sum([text.count(c) > 1 for c in set(text)]))