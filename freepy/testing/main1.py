def check_pass(pasw):
    check = [False,False,False]
    if len(pasw) > 10:
        return False
    if pasw is not str:
        return False
    for i in pasw:
        if i.islower(): check[0] = True
        if i.isupper(): check[1] = True
        if i.isdigit(): check[2] = True
    return all(check)


if __name__ == "__main__":
    print(check_pass("Asdfgl0"))