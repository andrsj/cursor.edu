
# Format Strings
	firstname = "Andrew"
	lastname = "Derkach"
	print(f"{firstname} [{lastname}]")

	# Format
	quantity = 3
	itemno = 567
	price = 49.95
	myorder = "I want {} pieces of item {} for {} dollars."
	print(myorder.format(quantity, itemno, price))

	# Length massive
	string = "string"
	print(len(string))

	# Methods
	var.upper()
	var.lower()
	var.find('p') // 0-9 - finded // -1 - not finded
	var.replace("first","second")
	print(var.strip()) #without space
	print(a.split(",")) # return масиви поділені комою



	table = {
		"1":111,
		"2":222,
		"3":333
	}
	for i,j in table.items():
		print(f"{i:10} ===> {j:10d}")

#########################################
#########################################
#########################################
#########################################

# FORMAT
	print("{0:d} - {0:x} - {0:o} - {0:b} ".format(21))
	>>> 21 - 15 - 25 - 10101

	>>> '{:<30}'.format('left aligned')
	'left aligned                  '
	>>> '{:>30}'.format('right aligned')
	'                 right aligned'
	>>> '{:^30}'.format('centered')
	'           centered           '
	>>> '{:*^30}'.format('centered')  # use '*' as a fill char
	'***********centered***********'

	>>> '{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
	'+3.140000; -3.140000'
	>>> '{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers
	' 3.140000; -3.140000'

	>>> # format also supports binary numbers
	>>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
	'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
	>>> # with 0x, 0o, or 0b as prefix:
	>>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
	'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

	>>> '{:,}'.format(1234567890)
	'1,234,567,890'

	>>> for align, text in zip('<^>', ['left', 'center', 'right']):
	...     '{0:{fill}{align}16}'.format(text, fill=align, align=align)
	...
	'left<<<<<<<<<<<<'
	'^^^^^center^^^^^'
	'>>>>>>>>>>>right'

	>>> width = 5
	>>> for num in range(5,12): 
	...     for base in 'dXob':
	...         print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
	...     print()
	...
		5     5     5   101
		6     6     6   110
		7     7     7   111
		8     8    10  1000
		9     9    11  1001
	   10     A    12  1010
	   11     B    13  1011


	d,i - ціле
	u - ?
	o - 8
	x - 16 з нижнім регістром
	X - 16 з верхнім регістром
	f - [-]1.0
	e - [-]1.0e+-1
	E - [-]1.0E+-1
	g,G - e|E if < 10 ** -4 else f
	s - стрічка
	r - та ж стрічка, що і поверне repr()
	c - 1 char
	% - % symbol


	x = 42
	r = ‘{0:10d}’.format(x) # r = ‘ 42’
	r = ‘{0:10x}’.format(x) # r = ‘ 2a’
	r = ‘{0:10b}’.format(x) # r = ‘ 101010’
	r = ‘{0:010b}’.format(x) # r = ‘0000101010’
	y = 3.1415926
	r = ‘{0:10.2f}’.format(y) # r = ‘ 3.14’
	r = ‘{0:10.2e}’.format(y) # r = ‘ 3.14e+00’
	r = ‘{0:+10.2f}’.format(y) # r = ‘ +3.14’
	r = ‘{0:+010.2f}’.format(y) # r = ‘+000003.14’
	r = ‘{0:+10.2%}’.format(y) # r = ‘ +314.16%’

	y = 3.1415926
	r = ‘{0:{width}.{precision}f}’.format(y,width=10,precision=3)
	r = ‘{0:{1}.{2}f}’.format(y,10,3)


	a = 42
	b = 13.142783
	c = “hello”
	d = {‘x’:13, ‘y’:1.54321, ‘z’:’world’}
	e = 5628398123741234
	r = “a is %d” % a # r = “a is 42”
	r = “%10d %f” % (a,b) # r = “ 42 13.142783”
	r = “%+010d %E” % (a,b) # r = “+000000042 1.314278E+01”
	r = “%(x)-10d %(y)0.3g” % d # r = “13 1.54”
	r = “%0.4s %s” % (c, d[‘z’]) # r = “hell world”
	r = “%*.*f” % (5,3,b) # r = “13.143”
	r = “e = %d” % e # r = “e = 5628398123741234”


	stock = {
		‘name’ : ‘GOOG’,
		‘shares’ : 100,
		‘price’ : 490.10 
	}
	r = “%(shares)d акций компаний %(name)s по цене %(price)0.2f” % stock
	# "100 акций компаний GOOG по цене 490.10

	name = “Едвард”
	age = 41
	r = “%(name)s, Возраст %(age)s год” % vars()


	r = “{0} {1} {2}”.format(‘GOOG’,100,490.10)
	r = “{name} {shares} {price}”.format(name=’GOOG’,shares=100,price=490.10)
	r = “Привет, {0}, ваш возраст {age} лет”.format(“Андрей”,age=47)


	stock = { 
		‘name’ : ‘GOOG’,
		‘shares’ : 100,
		‘price’ : 490.10 
	}
	r = “{0[name]} {0[shares]} {0[price]}”.format(stock)
	x = 3 + 4j
	r = “{0.real} {0.imag}”.format(x)