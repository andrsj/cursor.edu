# CLASSES

	# Method
		method.__doc__ 		# Doc
		method.__name__		# Ім'я методу
		method.__class__ 	# Class в якому визначений метод
		method.__func__		# Object of func що реалізує даний метод
		method.__self__		# Силка на екземпляр, асоціований з даним методом
							# None - для незв'язаних методів


	# Class
		c.__doc__				# Документація
		c.__name__				# Ім'я класу
		c.__bases__ 			# Кортеж з базовими класами
		c.__dict__				# Словник, що містить методи та атрибути класу
		c.__module__			# Ім'я  модулю, в ямоу визначений клас
		c.__abstractmetods__	# Множина імен абстрактних методів (None - якщо немає)


	# Example
		r.__class__ 	# Name class
		r.__dict__		# Словник, що містить дані про клас

	class Point:
        def __init__ (self, x, y)
            body of constr
            self.x = x
            self.y = y
        def function (self):
            body of function

	Initialization
	point = Point()
	point.function()

	class Animal:
	class Dog(Animal):
	class Cat(Animal):

	__lt__(self,other) self < other
	__le__(self,other) self <= other
	__gt__(self,other) self > other
	__ge__(self,other) self >= other
	__eq__(self,other) self == other
	__ne__(self,other) self != other


	__len__(self)      				# len(a) # a.__len__()
	__getitem__(self, key) 			# x = a[2] # x = a.__getitem__(2)
	__setitem__(self, key, value)	# a[1] = 7 # a.__setitem__(1,7)
	__delitem__(self, key)			# del a[2] # a.__delitem__(2)
	__contains__(self, obj)			# 5 in a # a.__contains__(5)

	# a = [1,2,3,4,5,6]
	# x = a[1:5] # x = a.__getitem__(slice(1,5,None))
	# a[1:3] = [10,11,12] # a.__setitem__(slice(1,3,None), [10,11,12])
	# del a[1:4] # a.__delitem__(slice(1,4,None))



	__add__(self,other) self + other
	__sub__(self,other) self - other
	__mul__(self,other) self * other
	__div__(self,other) self / other (Только в Python 2)
	__truediv__(self,other) self / other (Python 3)
	__floordiv__(self,other) self // other
	__mod__(self,other) self % other
	__divmod__(self,other) divmod(self,other)
	__pow__(self,other [,modulo]) self ** other, pow(self, other, modulo)
	__lshift__(self,other) self << other
	__rshift__(self,other) self >> other
	__and__(self,other) self & other
	__or__(self,other) self | other
	__xor__(self,other) self ^ other
	__radd__(self,other) other + self
	__rsub__(self,other) other - self
	__rmul__(self,other) other * self
	__rdiv__(self,other) other / self (Только в Python 2)
	__rtruediv__(self,other) other / self (Python 3)
	__rfloordiv__(self,other) other // self
	__rmod__(self,other) other % self
	__rdivmod__(self,other) divmod(other,self)
	__rpow__(self,other) other ** self
	__rlshift__(self,other) other << self
	__rrshift__(self,other) other >> self
	__rand__(self,other) other & self
	__ror__(self,other) other | self
	__rxor__(self,other) other ^ self
	__iadd__(self,other) self += other
	__isub__(self,other) self -= other
	__imul__(self,other) self *= other
	__idiv__(self,other) self /= other (Только в Python 2)
	__itruediv__(self,other) self /= other (Python 3)
	__ifloordiv__(self,other) self //= other
	__imod__(self,other) self %= other
	__ipow__(self,other) self **= other
	__iand__(self,other) self &= other
	__ior__(self,other) self |= other
	__ixor__(self,other) self ^= other
	__ilshift__(self,other) self <<= other
	__irshift__(self,other) self >>= other
	__neg__(self) –self
	__pos__(self) +self
	__abs__(self) abs(self)
	__invert__(self) ~self
	__int__(self) int(self)
	__long__(self) long(self) (Только в Python 2)
	__float__(self) float(self)
	__complex__(self) complex(self)


	#####################
	class foo:
        def normal_call(self):
            print("normal_call")
        def call(self):
            print("first_call")
            self.call = self.normal_call

    >>> y = foo()
	>>> y.call()
	first_call
	>>> y.call()
	normal_call
	>>> y.call()
	normal_call

	######################


class Circle(object):
	def __init__(self,radius):
		self.radius = radius

	@property
		def area(self):
			return math.pi*self.radius**2
	@property
		def perimeter(self):
			return 2*math.pi*self.radius

>>> c = Circle(4.0)
>>> c.radius
4.0
>>> c.area
50.26548245743669
>>> c.perimeter
25.132741228718345
>>> c.area = 2
Traceback (most recent call last):
File “<stdin>”, line 1, in <module>
AttributeError: can’t set attribute



class Foo(object):
	def __init__(self,name):
		self.__name = name
	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self,value):
		if not isinstance(value,str):
			raise TypeError("Ім'я повинне бути стрічкою")
		self.__name = value
	@name.deleter
	def name(self):
		raise TypeError("Неможливо видалити атрибут Ім'я")

>>> f = Foo("Гвидо")
>>> n = f.name # викличе f.name() – поверне функцію
>>> f.name = "Монти" # викличе метод зміни name(f,”Монти”)
>>> f.name = 45 # викличе метод зміни name(f,45) -> TypeError
>>> del f.name # викличе метод видалення name(f) -> TypeError






class TypedProperty(object):
	def __init__(self,name,type,default=None):
		self.name = "_" + name
		self.type = type
		self.default = default if default else type()
	def __get__(self,instance,cls):
		return getattr(instance,self.name,self.default)
	def __set__(self,instance,value):
		if not isinstance(value,self.type):
			raise TypeError("Значення повинно бути типом %s" % self.type)
		setattr(instance,self.name,value)
	def __delete__(self,instance):
	raise AttributeError("Неможливо видалити атрибут")

class Foo(object):
	name = TypedProperty(“name”,str)
	num = TypedProperty(“num”,int,42)

f = Foo()
a = f.name # Неявно викличе метод Foo.name.__get__(f,Foo)
f.name = “é«¬” # Викличе Foo.name.__set__(f,”Guido”)
del f.name # Викличе Foo.name.__delete__(f)






class A(object):
	def __init__(self):
		self.__X = 3 # Буде змінено на self._A__X
	def __spam(self): # Буде змінено на _A__spam()
		pass
	def bar(self):
		self.__spam() # Викличе тільки метод A.__spam()

class B(A):
	def __init__(self):
		A.__init__(self)
		self.__X = 37 # Буде змінено на self._B__X
	def __spam(self): # Буде змінено на _B__spam()
		pass



from abc import ABCMeta, abstractmethod, abstractproperty
class Foo(metaclass = ABCMeta):
	@abstractmethod
	def spam(self,a,b):
		pass
	@abstractproperty
	def name(self):
		pass

>>> f = Foo()
Traceback (most recent call last):
File “<stdin>”, line 1, in <module>
TypeError: Can’t instantiate abstract class Foo with abstract methods spam