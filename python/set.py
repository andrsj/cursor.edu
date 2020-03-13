# Набори SET
	thisset = {"apple", "banana", "cherry"}
	thisset.add("orange")							#| додає елемент в набір
	thisset.update(["orange", "mango", "grapes"])	#| додає масив в набір

	set1 = {"a", "b" , "c"}
	set2 = {1, 2, 3}
	set3 = set1.union(set2)  	#| об'єднання наборів

	set1.update(set2) 			#| додавання набору в набір
	print(set1)


	# Set — множество, в котором отсутствуют повторяющиеся элементы:
	>>> a = set([1,2,3,4])
	>>> b = set([3,4,5,6])
	>>> a | b # Объединение
	{1, 2, 3, 4, 5, 6}
	>>> a & b # Пересечение
	{3, 4}
	>>> a < b # Подмножества
	False
	>>> a - b # Разница
	{1, 2}
	>>> a ^ b # Симметрическая разность
	{1, 2, 5, 6}

	first = {1, 2, 3, 4, 5, 6}
	second = {4, 5, 6, 7, 8, 9}

	print(first | second)
	print(first & second)
	print(first - second)
	print(second - first)
	print(first ^ second)

	# OUT:
	# {1, 2, 3, 4, 5, 6, 7, 8, 9}
	# {4, 5, 6}
	# {1, 2, 3}
	# {8, 9, 7}
	# {1, 2, 3, 7, 8, 9}

	# Обе функции union () и update () исключают любые повторяющиеся элементы.

	add () 							# Добавляет элемент в набор
	clear () 						# Удаляет все элементы из набора
	copy () 						# Возвращает копию набора
	difference () 					# Возвращает набор, содержащий различие между двумя или более наборами
	diff_update () 					# Удаляет элементы в этом наборе, которые также включены в другой, указанный набор
	discard () 						# Удалить указанный элемент
	intersection () 				# Возвращает множество, то есть пересечение двух других множеств
	intersection_update () 			# Удаляет элементы в этом наборе, которых нет в других, указанных наборах
	isdisjoint () 					# Возвращает ли пересечение двух наборов или нет
	issubset () 					# Возвращает, содержит ли другой набор этот набор или нет
	issperset () 					# Возвращает, содержит ли этот набор другой набор или нет
	pop () 							# Удаляет элемент из набора
	remove () 						# Удаляет указанный элемент
	mmetric_difference () 			# Возвращает набор с симметричными разностями двух наборов
	mmetric_difference_update ()    # Вставляет симметричные отличия от этого набора и другого
	union () 						# Возвращает набор, содержащий объединение множеств
	update () 						# Обновите набор с объединением этого набора и других