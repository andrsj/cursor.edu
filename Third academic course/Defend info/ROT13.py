def rot13(message):
    res = ""
    for i in message:
        if 65 <= ord(i) <= 77 or 97 <= ord(i) <= 109: res += chr(ord(i) + 13)
        elif 78 <= ord(i) <= 90 or 110 <= ord(i) <= 122: res += chr(ord(i) - 13)
        else: res += i
    return res


if __name__ == '__main__':
    inpt = "EBG13 rknzcyr."
    output = "ROT13 example."
    print(rot13(output), rot13(inpt), rot13(inpt) == output)