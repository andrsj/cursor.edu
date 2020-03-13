# MODULES
	m.__dict__  # Атрибути модуля
	m.__doc__  	# Doc
	m.__name__	# Name
	m.__file__	# File
	m.__path__	# Path


# module: spam.py
__all__ = [ ‘bar’, ‘Spam’ ]
# Ці імена будуть імпортовані при команді from spam import *

# Перевірити, чи модуль був запущений як програма
if __name__ == "__main__":
	pass
else:
	# Файл, був імпортований як модуль
	pass










# Copy
copy()
deepcopy()




# sys
sys.float_info
sys.maxsize
sys.path

sys:
stdout | stdin | stderr





# Decimal

import decimal
x = decimal.Decimal("3.4")
y = decimal.Decimal("4.5")

a = x * y 	# a = decimal.Decimal(‘15.30’)
b = x / y 	# b = decimal.Decimal(‘0.7555555555555555555555555556’)

decimal.getcontext().prec = 3
c = x * y 	# c = decimal.Decimal(‘15.3’)
d = x / y 	# d = decimal.Decimal(‘0.756’)

a = decimal.Decimal(42) # Створить Decimal("42")
b = decimal.Decimal("37.45") # Створить Decimal("37.45")
c = decimal.Decimal((1,(2,3,4,5),-2)) # Створить Decimal("-23.45")
d = decimal.Decimal("Infinity")
e = decimal.Decimal("NaN")

x.exp()
x.ln()
x.log10()
x.sqrt()




# Fractions

>>> f = fractions.Fraction(3,4)
>>> f
Fraction(3, 4)
>>> g = fractions.Fraction(“1.75”)
>>> g
Fraction(7, 4)
>>> h = fractions.Fraction.from_float(3.1415926)
Fraction(3537118815677477, 1125899906842624)
>>>









# Datetime

	import datetime
	x = datetime.datetime.now()
	print(x) 

	print(x.strftime("%_")) 
	VVVVVVVVVVVVVVVVVVVVVVVV
	%a 	Weekday, short version 						Wed 	
	%A 	Weekday, full version 						Wednesday 	
	%w 	Weekday as a number 0-6, 0 is Sunday 		3 	
	%d 	Day of month 01-31 							31 	
	%b 	Month name, short version 					Dec 	
	%B 	Month name, full version 					December 	
	%m 	Month as a number 01-12 					12 	
	%y 	Year, short version, without century 		18 	
	%Y 	Year, full version 							2018 	
	%H 	Hour 00-23 									17 	
	%I 	Hour 00-12 									05 	
	%p 	AM/PM 										PM 	
	%M 	Minute 00-59 								41 	
	%S 	Second 00-59 								08 	
	%f 	Microsecond 000000-999999 					548513 	
	%z 	UTC offset 									+0100 	
	%Z 	Timezone 									CST 	
	%j 	Day number of year 001-366 					365 	
	%U 	Week number of year, Sunday as the first day of week, 00-53 	52 	
	%W 	Week number of year, Monday as the first day of week, 00-53 	52 	
	%c 	Local version of date and time 				Mon Dec 31 17:41:00 2018 	
	%x 	Local version of date 						12/31/18 	
	%X 	Local version of time 						17:41:00 	
	%% 	A % character 								%