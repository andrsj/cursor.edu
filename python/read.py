# Зчитування з файлу
	f = open("demofile.txt", "r")
	print(f.read(*к-сть символів*)) 		#| Зчитування символів (або всього тексту)
	print(f.readline()) 					#| Зчитування рядку

	f = open("demofile.txt", "r")			#| Зчитування з файлу з рядка по рядок
	for x in f:
		print(x) 

	f = open("demofile.txt", "a")			#| Добавить в кінець
	f = open("demofile.txt", "w") 			#| Перезапише файл
	f = open("demofile.txt", "x") 			#| Створить файл (при його існуванні - помилка)
	f.write("Now the file has more content!")

	f.close()								#| Закриття файлу

#############################################################################

	f = open("data.txt")
	lines = (t.strip() for t in f) # Прочитать строки и удалить пробелы
	comments = (t for t in lines if t[0] == "#") # Коментарии

#############################################################################

	lines = open(“portfolio.txt”)
	fields = (line.split() for line in lines)
	print(sum(float(f[1]) * float(f[2]) for f in fields))

#############################################################################

	fields = (line.split() for line in open(“portfolio.txt”))
	portfolio = [ 
		{
			‘name’ : f[0],
			‘shares’ : int(f[1]),
			‘price’ : float(f[2]) 
		}
		for f in fields]

	msft = [s for s in portfolio if s[‘name’] == ‘MSFT’]
	large_holdings = [s for s in portfolio
	if s[‘shares’]*s[‘price’] >= 10000]