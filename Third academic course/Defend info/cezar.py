alphabet = 'abcdefghijklmnopqrstuvwxyz'


def cezar(input_text:str, output_text:str) -> str:
    print('\nCezar work:')
    key = 0
    for i in range(1,26):
        decode_text = ''
        for letter in input_text:
            index = (alphabet.index(letter) + i) % 26
            decode_text += alphabet[index]
            if decode_text == output_text:
                key = i
        print(decode_text, decode_text == output_text, f'Key = {i}')
    decode_text = ''
    print(f'Key = {key}')
    print('End Cezar work')
    return key


def cezar_key(input_text:str, key:int, code:bool = True) -> str:
    print('\nCezar_key work:')
    decode_text = ''
    print('Index: ', end=' ')
    for letter in input_text:
        a = alphabet[::-1] if not code else alphabet
        index = (a.index(letter) + key) % 26
        print(index, end=' ')
        decode_text += a[index]

    print(f'\nCoded text: \'{decode_text}\'')
    print('End Cezar_key work')
    return decode_text


if __name__ == "__main__":
    one = 'abcdef', 'tuvwxy'
    two = 'abcdefghijklmnopqrstuvwxyz', 'tuvwxyzabcdefghijklmnopqrs'
    three = 'world', 'dvysk'

    elem = two

    key = cezar(elem[0], elem[1])
    from_input_to_out = cezar_key(elem[0], key)
    print(f'\nCheck work function: {from_input_to_out == elem[1]} \t \'{elem[0]}\' -> \'{elem[1]}\'\n')
    from_out_to_input = cezar_key(elem[1], key, False)
    print(f'\nCheck work function: {from_out_to_input == elem[0]} \t \'{elem[1]}\' -> \'{elem[0]}\'')