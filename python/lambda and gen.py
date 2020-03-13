# Lambda Map Filter Generators
	nums = [11, 22, 33, 44, 55]
	result = list(map(lambda x: x+5, nums))
	print(result)


	squares = map(lambda a: a*a, [1,2,3,4,5])
	# теперь squares = [1,4,9,16,25]

	numbers = [1,2,3,4,5]
	squares = map(lambda x: x*x, numbers)
	# теперь squares = [1,4,9,16,25]

	numbers = [1,2,3,4,5]
	squares = [number*number for number in numbers]
	# и снова squares = [1,4,9,16,25]

	numbers = [1,2,3,4,5]
	numbers_under_4 = [number for number in numbers if number < 4]
	# numbers_under_4 = [1,2,3]

	numbers = [1,2,3,4,5]
	squares = [number*number for number in numbers if number < 4]
	# square = [1,4,9]

	Синтаксис генератора списков: [ element for variable(s) in list if condition ]
	list — любой итерируемый элемент
	variable(s) — переменная или переменные, которые приравниваются к текущему элементу списка, аналогично циклу for
	condition — инлайновое выражение: если оно равно true, элемент добавляется в результат
	element — инлайновое выражение, результат которого используется как элемент списка-результата

	
	numbers = (1,2,3,4,5)
	squares_under_10 = (number*number for number in numbers if number*number < 10)
	for square in squares_under_10:
    print square,
	#выводит '1 4 9'


	nums = [11, 22, 33, 44, 55]
	res = list(filter(lambda x: x%2==0, nums))  # Function need return True or False
	print(res)


	a = [-3,5,2,-10,7,8]
	b = ‘abc’

	e = [(x,y) for x in a 		# e = [(5,’a’),(5,’b’),(5,’c’),
	for y in b 					# (2,’a’),(2,’b’),(2,’c’),
	if x > 0 ] 					# (7,’a’),(7,’b’),(7,’c’),
								# (8,’a’),(8,’b’),(8,’c’)]

	f = [(1,1),(2,2),(3,3)]
	g = [x + y for x,y in f]
	# [2,4,6]

	>>> a = [1, 2, 3, 4]
	>>> b = (10*i for i in a)
	>>> b
	<generator object at 0x590a8>
	>>> b.next()
	10
	>>> b.next()
	20


	def countdown(n):
	print("Обернений відлік з %d" % n)
	try:
		while n > 0:
		yield n
		n = n - 1
	except GeneratorExit:
		print("Досягнено значення %d" % n)


	>>> a = "lsj94ksd231 9"
	>>> b = [int(i) for i in a if '0'<=i<='9']
	>>> b
	[9, 4, 2, 3, 1, 9]