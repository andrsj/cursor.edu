s = 'ABCDEFGHIJKLM'
print(s[0],ord(s[0]),s[-1],ord(s[-1]))
c1 = ""
for i in s:
    c1 += chr(ord(i) + 13)
s = s.lower()
print(s[0],ord(s[0]),s[-1],ord(s[-1]))
c2 = ""
for i in s:
    c2 += chr(ord(i) + 13)
s = "NOPQRSTUVWXYZ"
print(s[0],ord(s[0]),s[-1],ord(s[-1]))
c3 = ""
for i in s:
    c3 += chr(ord(i) - 13)
s = s.lower()
print(s[0],ord(s[0]),s[-1],ord(s[-1]))
c4 = ""
for i in s:
    c4 += chr(ord(i) - 13)

print(c1)
print(c2)
print(c3)
print(c4)

for i in range(10):
    print(ord(str(i)))

a = ""
for i in list(range(48,57 + 1)) + list(range(65,90 + 1)) + list(range(97,122 + 1)):
    a += chr(i)
print(a)


def alphanumeric(password):
    for i in password:
        if not 48 <= ord(i) <= 57 and not 65 <= ord(i) <= 90 and not 97 <= ord(i) <= 122:
            return False
    return bool(password)
