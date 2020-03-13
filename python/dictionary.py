# Objects | Словники


	>>> {a:a**2 for a in range(1, 10)}
	{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

	name_object = {
        "name": "Andrew",
        "age": 20,
        "cool": True
	}

	name_object.get("var") 						# | повертає значення, якщо воно є, якщо ні - None
	name_object.get("var", "value") 		 	# | повертає значення для ключа var, якщо таке є, інакше повертає "value"
	name_object["name"] = "Bogdan"
	name_object["new var"] = "new var value" 	# -> Створить нове поле для цього об'єкту

	# Example
	d = dict(zero='Cero', one='Uno', two='Dos', three='Tres', four='Cuatro', five='Cinco', six='Seis', seven='Siete', eight='Ocho', night='Nueve')

	for index, (key, value) in enumerate(d.items()):
        print(f"{index} is {key} in England and {value} in Spain")

	for key,value in dictionary.items():
		...


	# Створення словника з 2х списків
    >>> t1 = (1, 2, 3)
	>>> t2 = (4, 5, 6)
	>>> dict (zip(t1,t2))
	{1: 4, 2: 5, 3: 6}



	# Описание метода
	clear () 		# Удаляет все элементы из словаря
	copy () 		# Возвращает копию словаря
	fromkeys () 	# Возвращает словарь с указанными ключами и значениями
	get () 			# Возвращает значение указанного ключа
	items () 		# Возвращает список, содержащий кортеж для каждой пары ключ-значение
	keys () 		# Возвращает список, содержащий ключи словаря
	pop () 			# Удаляет элемент с указанным ключом
	popitem () 		# Удаляет последнюю вставленную пару ключ-значение
	setdefault () 	# Возвращает значение указанного ключа. Если ключ не существует: введите ключ с указанным значением
	update () 		# Обновляет словарь с указанными парами ключ-значение
	values () 		# Возвращает список всех значений в словаре


	Сортировка словаря
	>>> # Не сортированный словарь
	>>> d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
	>>> # Словарь сортирован по ключ
	>>> OrderedDict(sorted(d.items(), key=lambda t: t[0]))
	OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
	>>> # Сортировка по значениям
	>>> OrderedDict(sorted(d.items(), key=lambda t: t[1]))
	OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
	>>> # Сортировка по длине названия ключа
	>>> OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
	OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])



	# Сортировка по ключах через lambda

	elist = [{"a":1,"b":5},{"a":2,"b":4},{"a":3,"b":3}]
	elist.sort( key = lambda x : x["b"])


	###################################
	dictionary = {"a": 1, "b": 2}

	def some_function(a, b):
        print(a + b)
        return

	# оба варианта делают одно и то же:
	some_function(**dictionary)
	some_function(a=1, b=2)