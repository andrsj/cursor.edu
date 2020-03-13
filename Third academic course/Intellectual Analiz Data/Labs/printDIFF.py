import sympy
x, y = sympy.symbols('x y')
# print(sympy.diff(sympy.exp(x) + x**2))
print(sympy.diff(1 / (1 + sympy.exp(-x))))