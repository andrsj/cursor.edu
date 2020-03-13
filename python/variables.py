a_int = 5
b_double = 5.1
c_string = "string"
d_bool = False

f_longstring = '''Start
Mid
End'''


def compare(a,b):
    if a is b:
        pass
    if a == b:
        pass
    if type(a) is type(b):
        pass

if type(s) is list:
    pass


None
x = "Hello World" 								str
x = 20 											int 	
x = 20.5 										float 	
x = 1j 											complex 	
x = ["apple", "banana", "cherry"] 				list 	
x = ("apple", "banana", "cherry") 				tuple 	
x = range(6) 									range 	
x = {"name" : "John", "age" : 36} 				dict 	
x = {"apple", "banana", "cherry"} 				set 	
x = frozenset({"apple", "banana", "cherry"}) 	frozenset 	
x = True 										bool 	
x = b"Hello" 									bytes 	
x = bytearray(5) 								bytearray 	
x = memoryview(bytes(5)) 						memoryview

1.7e3 = 1700



print(a_int, b_double, c_string, d_bool, f_longstring)
print(c_string[0]) // "s"
print(c_string[-1]) // "g"
print(c_string[0:3]) // "str"
print(c_string[:3]) // "str"
print(c_string[1:]) // "tring"
print(c_string[2:-1]) // "ring"
print(len(c_stirng))




# Converting
	int()
	float()
	bool()
	number1 = int(input("Enter first number: "))
	number2 = int(input("Enter second number: "))
	print("Summ: " + str((number1 + number2)))


# GetTypes
	print("Type a: " + str(type(a_int)))