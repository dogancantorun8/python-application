import sympy as sym
import numpy as np

sym.init_printing()

x = sym.Symbol('x')

result = sym.solve(x ** 3 - 3 * x ** 2 + 2)
print(result)
e = x ** 2 * (1 - sym.cos(2 / x))
print(e)

#limit hesaplaması
result = sym.limit(e, x, np.inf)
print(result)
result = sym.limit(e, x, 0)
print(result)

#solve ile denklem çözümü:
x, a, b, c = sym.symbols('x, a, b, c')
e = a * x ** 2 + b * x + c
result = sym.solve(e, x)
print(result)

#x yerine 2 y yerine 4 yazdım
x, y = sym.symbols('x, y')
e = sym.sin(2 * x ** 3) + sym.log(3 * x * y) + x - y
f = e.subs(x, 2).subs(y, 4)
result = f.evalf()
print(result)

#sembolik işlem yapıp en son değer atama
sym.init_printing()
x, y = sym.symbols('x, y')
e = sym.integrate(sym.sin(x), x)
result = e.evalf(subs={'x': 2})
print(result)

#determinant alırsam
sym.init_printing()
a, b = sym.symbols('a b')
m = sym.Matrix([[a, 2], [b, 5]])
result = m.det()
result = result.subs(a, 2).subs(b, 3)
print(result.evalf())


#plot operasyon
x = sym.Symbol('x')
f = x ** 2
sym.plot(f)

#plot ops:sinüs eğrisi çizdim
x = sym.Symbol('x')
#f = x ** 3 - 3 * x ** 2 + 2
f = sym.sin(x)
sym.plot(f, line_color='red', xlabel='x values', ylabel='y values')

#iki tane grafiğin gösterimi
x = sym.Symbol('x')
f1 = x
f2 = sym.sin(x)
p = sym.plot(f1, line_color='red', xlabel='x values', ylabel='y values', legend=True, show=False)
p.extend(sym.plot(f2, line_color='blue', xlabel='x values', ylabel='y values', legend=True, show=False))
p.show()


#3d grafik çizim
x = sym.Symbol('x')
f1 = x
f2 = sym.sin(x)
p = sym.plot(f1, title='Some math functions', line_color='red', xlabel='x values', ylabel='y values', legend=True, show=False)
p.extend(sym.plot(f2, line_color='blue', xlabel='x values', ylabel='y values', legend=True, show=False))
y = sym.Symbol('y')
sym.plotting.plot3d(x ** 2 + y)
p.show()
