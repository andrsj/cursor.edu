import random as rand

a1 = a2 = a3 = a4 = a5 = a6 = 0

number = int (input("Enter number: "))

i = 1

while i <= number :
    a = rand.randint(1,6)
    if a == 1:
        a1 += 1
    elif a == 2:
        a2 += 1
    elif a == 3:
        a3 += 1
    elif a == 4:
        a4 += 1
    elif a == 5:
        a5 += 1
    elif a == 6:
        a6 += 1
    i += 1

print("1: " + str(a1/number) + "\n2: " + str(a2/number) + 
"\n3: " + str(a3/number) + "\n4: " + str(a4/number) + 
"\n5: " + str(a5/number) + "\n6: " + str(a6/number)) 
print("Done")