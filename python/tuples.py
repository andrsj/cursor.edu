# Кортежі
	coord = (1,2,3)
	x,y,z = coord  # | x - 1 | y - 2 | z - 3
	x,y,_ = coord  # | x - 1 | y - 2 | None

	lol = (1,2,3,4,5)
	a,b,*c = lol 
	OUT:
		1
		2
		[3,4,5]

	a,b,*c,d = lol
	OUT:
		1
		2
		[3,4]
		5


	>>> from collections import namedtuple
	>>> NetworkAddress = namedtuple(‘NetworkAddress’,[‘hostname’,’port’])
	>>> a = NetworkAddress(‘www.python.org’,80)
	>>> a.hostname
	‘www.python.org’
	>>> a.port
	80
	>>> host, port = a
	>>> len(a)
	2
	>>> type(a)
	<class ‘__main__.NetworkAddress’>
	>>> isinstance(a, tuple)
	True