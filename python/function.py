# Functions

	f.__doc__  		#- стрічка документації
	f.__name__ 		#- назва функції
	f.__dict__ 		#- словник, що містить атрибути функції
	f.__code__ 		#- скомпільований байт код функції
	f.__defaults__ 	#- кортеж з аргументами по заумовчуванню
	f.__globals__  	#- словник, що містить глобальні простори імен
	f.__closure__ 	#- кортеж, що містить дані, зв'язані з вкладеними областями видимості

	def func(a:int , b:bool) -> int:
		return a * b

	def Name_Function ( ) :
	    Body_Function
	    return var

	# Parametrs

	function(a,b)				#| просто параметри
	function(b = b , a = a)  	#| значення за умовчуванням
	function(*parametrs)		#| якщо невідомо скільки буде параметрів

		print(parametrs[10])

	x = lambda arguments : expression
	# Like 		
		def func(arguments):
			return expression


	# Example

	def myfunc(n):
	  return lambda a : a * n

	mydoubler = myfunc(2)
	mytripler = myfunc(3)

	print(mydoubler(11))   		#| 22
	print(mytripler(11))		#| 33





	def foo(x, items=[]):
		items.append(x)
		return items

	foo(1) # return [1]
	foo(2) # return [1, 2]
	foo(3) # return [1, 2, 3]





	a = [1, 2, 3, 4, 5]
	def square(items):
		for i,x in enumerate(items):
			items[i] = x * x 
	square(a)
	# return => [1,4,9,16,25]



def f(x,l=[]): 
    for i in range(x): 
        l.append(i*i) 
    print(l)

f(2) 
f(3,[3,2,1])
f(3)