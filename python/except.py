# EXCEPT

	try:
		pass
	except IOError as e:
		pass
	...
	except TypeError as e:
		pass
	...
	except NameError as e:
		pass
	...
	else:
		pass
	finally:
		pass



	try:
		pass
	except Exception as e:
		error_log.write("Виникла помилка: %s\n" % e)



BaseException
# Базовий клас

Exception
# Базовий клас для всіх програмний виключень
# Враховуючи всі встроїні 
#! Крім SystemExit, GeneratorExit, KeyboardInterrupt

ArithmeticError
# Базовий клас для виключень для арифметичних операцій
#? OverFlowError, ZeroDivisionError, FloatingPointError

LookupError
# Базовий клас для виключень, виникаючих при доступу до 
# недоступного індексу чи ключу
#? IndexError, KeyError

EnvironmentError
# Базовий клас для помилок поза інтрепретатором
#? IOError, OSError

AssertionError
# Не виконано умова в інструкції assert

AttributeError
EOFError
FloatingPointError
GeneratorExit

IOError
# Помилка вводу-виводу
# From EnvironmentError

ImportError
IndentationError
IndexError
KeyError

KeyboardInterrupt
# Ctrl + C в консолі

MemoryError
NameError

NotImplementedError
# Нереалізована особливість

OSError
# Помилка ОС

OverflowError
# Занадто велике ціле число

ReferenceError
# Звернення по слабій силці #?

RuntimeError
# Помилка, що не підлягає ні під одну категорію

StopIteration
SyntaxError
SystemError
SystemExit
TypeError

UnboundLocalError
# Спроба звернення до незв'язаної локальної змінної
# Ця помилка виникає при змозі звернутися до змінної
# до того, як вона буде оприділена в функції

UnicodeError
UnicodeEncodeError
UnicodeDecodeError
UnicodeTranslateError

ValueError
WindowsError
ZeroDivisionError
