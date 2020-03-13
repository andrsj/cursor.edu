def solution(s):
    return [i+j for i,j in zip(s[::2],s[1::2])] if len(s[::2]) == len(s[1::2]) else [i+j for i,j in zip(s[::2],s[1::2])] + [s[-1] + "_"]

def solution1(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]

def solution2(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]

import re
def solution3_re(s):
    return re.findall('..', s + '_')

def solution4(s):
    return ['{:2}'.format(s[x:x+2]).replace(' ','_') for x in range(0,len(s),2)]

print(solution("asdfasdf"))
print(solution("asdfasd"))
print(solution(""))
print(solution("x"))