	/////////////////////////////////
	print(1 == True)    # True
	print(1 is True)    # False

	print(id(1))        # 10943008
	print(id(True))     # 10262944

	print(int.__subclasses__()) # -> [<class 'bool'>]

	//////////////////////////////////
	''.join(map(str, [1, 2, 3, 4, 5]))
	'12345'

	' '.join(map(lambda x: str(x**2), [1, 2, 3, 4, 5]))
	'1 4 9 16 25'


	//////////////////////////////////
	books = [["Sherlock Holmes", "Arthur Conan Doyle", 1986, True, 12.51],
            ["The Lost World", "Arthur Conan Doyle", 2015, False, 5.95],
            ["The Art of Computer Programming", "Donald E. Knuth ", 2017, True, 190.54] ]

	TITLE_AUTHOR = slice(0, 2)
	PRICE_IN_STOCK = slice(3, 5)
	print(books[0][TITLE_AUTHOR])
	print([book for book in books if book[PRICE_IN_STOCK] > [True, 10.0]])
	//////////////////////////////////

	recent_presidents = ['Борис Ельцин', 'Владимир Путин', 'Дмитрий Медведев']
	print 'Последними президентами были %s.' % ', '.join(recent_presidents)
	# печатает "Последними президентами были Борис Ельцин, Владимир Путин, Дмитрий Медведев."
	//////////////////////////////////
	Назначение переменных по условию
	x = 1 if (y == 10) else 2 # X равно 1, при условии, что Y равен 10. Если это не так - X равен 2
	x = 3 if (y == 1) else 2 if (y == -1) else 1  # Более длинное условие. Не используйте здесь elif


	//////////////////////////////////

	>>> a = 10
	>>> b = 5
	>>> a, b
	(10, 5)
	>>> a, b = b, a
	>>> a, b
	(5, 10)

	//////////////////////////////////

	Срезы в списках и работа с ними
	>>> a = range(10)
	>>> a
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	>>> a[:5] = [42] # Все символы до 5 заменяются элементом "42"
	>>> a
	[42, 5, 6, 7, 8, 9]
	>>> a[:1] = range(5) 
	>>> a
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	>>> del a[::2] # Удаление каждого второго элемента
	>>> a
	[1, 3, 5, 7, 9]
	>>> a[::2] = a[::-2] # Альтернатива reserved
	>>> a
	[9, 3, 5, 7, 1]
	//////////////////////////////////
	# Подсчет количества элементов (в примере — количество букв в слове):
	from collections import Counter
	Counter('habrahabr')  # Counter({'a': 3, 'h': 2, 'r': 2, 'b': 2})
	//////////////////////////////////

	items = [2, 2, 3, 3, 1]
	print(list(set(items)))
	# [1, 2, 3]

	//////////////////////////////////