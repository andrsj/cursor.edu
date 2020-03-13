# Primitive Math
10 + 3 | 10 - 3 | 10 * 3 | 10 / 3 = 3.333 |
10 // 3 = 3 | 10 % 3 = 1 | 10 ** 3 = 10^3 |
	
# Bytes
x << y  # left
x >> y 	# right
x & y 	# and
x | y 	# or
x ^ y 	# nor
~x 		# no

abs(x) 			=> abs 
divmod(x,y)  	=> (x // y , x % y) #!
pow(x,y [ , modulo]) => (x ** y) % modulo
round(x,[n]) 	=> x * 10 ** -n

	>>> round(1234.5678, -2)
	1200.0
	>>> round(1234.5678, 2)
	1234.57

print(round(var)) 		# 2.9 = 3
print(abs(var)) 		# |var| -2.9 = 2.9



# pow
	def power(x, y):
		if y == 0:
			return 1
		else:
			return x * power(x, y-1)

	print(power(2, 3))