
# Massive + methods + SLICE

	massive.append(var) 			#| в кінець
	massive.insert(index, var) 		#| на місці індекса вставити елемент
	massive.remove(var) 			#| видалити елемент з масиву
	massive.clear() 				#| очистити
	massive.pop() 					#| повертає останній елемент і видаляє його з масиву
	massive.index(var) 				#| повертає індекс елементу
	massive.count(var) 				#| повертає к-сть var в масиві
	massive.sort() 					#| сортує масив
	massive.reverse() 				#| реверс масиву
	massive2 = massive1.copy() 		#| копіювання масиву
	massive2 = list(massive1)		#| копіювання масиву
	del thislist[0] 				#| видаляє вказаний елемент по індексу
	del thislist					#| видаляє список


	# Додавання масивів
	list1 = ["a", "b" , "c"]
	list2 = [1, 2, 3]
	list3 = list1 + list2

	l + ll 				# Конкатенація
	l * n | n * l 		# n копій
	v1,v2, ... , vn = l # Розпаковка
	x in s | x not in s # Перевірка на вхід
	all(s)				# True якщо всі не False
	any(s)				# True якщо хоча б один True






	print(c_string[0]) // "s"
	print(c_string[-1]) // "g"
	print(c_string[0:3]) // "str"
	print(c_string[:3]) // "str"
	print(c_string[1:]) // "tring"
	print(c_string[2:-1]) // "ring"

	a = m[0:100:10] 
	b = m[1:10, 3:20] 
	c = m[0:100:10, 50:75:5]
	m[0:5, 5:10] = n
	del m[:10, 15:] 
	a = m[..., 10:20]
	m[10:20, ...] = n


	a = [1,2,3,4,5]
	>>> a[::2]  # Указываем шаг
	[1,3,5]
	>>> a[::-1] # Переворачиваем список
	[5,4,3,2,1]

	a = list(range(5))
	print(" ".join(str(i) for i in a)) # -> 0 1 2 3 4



###############################################
	>>> a = [3,4,5]
	>>> b = [a]
	>>> c = 4*b
	>>> c
	[[3, 4, 5], [3, 4, 5], [3, 4, 5], [3, 4, 5]]
	>>> a[0] = -7
	>>> c
	[[-7, 4, 5], [-7, 4, 5], [-7, 4, 5], [-7, 4, 5]]
	>>>


# Удаление дубликатов!	
	items = [2, 2, 3, 3, 1]
	print(list(set(items)))
	# [1, 2, 3]

# COPY
	li = [1,2,3]
	new_li = [:]
	print (li is new_li)
	>>> False



	>>> a = [ 1, 2, [3,4] ]
	>>> b = list(a) # поверхнева копія
	>>> b is a
	False
	>>> b.append(100)
	>>> b
	[1, 2, [3, 4], 100]
	>>> a
	[1, 2, [3, 4]]
	>>> b[2] [0] = -100  # зміна внутрішнього списку
	>>> b
	[1, 2, [-100, 4], 100]
	>>> a 
	[1, 2, [-100, 4]]
	>>>
	



############################################
	# Нумеровані списки
	for i, item in enumerate(['a', 'b', 'c']):
    print(i, item)

	# 0 a
	# 1 b
	# 2 c


	for i, item in enumerate(['a', 'b', 'c'], 1): # 1 - start iteration
    print(i, item)

	# 1 a
	# 2 b
	# 3 c
