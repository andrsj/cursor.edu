def cezar_period(word:str, key:tuple) -> str:
    keys = [i for i in range(1,len(key) + 1)]
    for i in key:
        if i in keys:
            keys.remove(i)
    if keys:
        print('Wrong key!')
        return


    print(f"'{word}'")
    if len(word) % len(key): 
        for _ in range(len(key) - len(word) % len(key)): word += ' '
    w = [word[i:i+len(key)] for i in range(0,len(word), len(key))]

    print(f'Arrays:')

    res = ''
    for i in w:
        for j,k in zip(i,key):
            print(f'Letter \'{j}\' \t Key -> {k} | Code -> \'{i[k - 1]}\'')
            # if i[k - 1] != ' ': 
            res += i[k - 1]
    print(f'Result code -> \'{res}\'')
    return res

if __name__ == "__main__":
    one = 'Andrew  ', 'dArn e w', (3,1,4,2)
    two = 'Andrew', 'dAnrew', (3,1,2,4)

    decode = cezar_period(one[0], one[2])
    print(f'\nDecoded text -> \'{decode}\'', '\t Input == Code(Output) -> ', decode == one[1])

    decode = cezar_period(one[1], one[2][::-1])
    print(f'\nEncoded text -> \'{decode}\'', '\t Output == Code(Input) -> ', decode == one[0])