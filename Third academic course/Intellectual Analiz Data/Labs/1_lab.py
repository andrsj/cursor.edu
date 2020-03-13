a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a<=0 or b<=0 or c<=0 :
    print("Помилкові вхідні дані")
else :
    if a + b > c and a + c > b and b + c > a :
        print("Це є трикутник")
        if (a**2 + b**2) == c**2 or (a**2 + c**2) == b**2 or (b**2 + c**2) == a**2:
            print("Трикутник прямокутний")
        else :
            print("Трикутник не є прямокутний")
    else :
        print("Це не є трикутник")



