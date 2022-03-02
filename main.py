import math
import numpy
from scipy import integrate
import matplotlib.pyplot as plt

print('Задание №1')
array = numpy.random.randint(1, 10, size=(5, 5))
print(array)
array_transpose = numpy.transpose(array)
print(array_transpose)
print(numpy.linalg.det(array_transpose))
print('Задание №2')
array_1 = numpy.random.randint(1, 10, size=(3, 1))
print(array_1)
array_2 = numpy.random.randint(1, 10, size=(3, 2))
rez = array_1 * array_2
print(array_2)
print(rez)
print('Задание №3')
M1 = numpy.array([[1, 0, -1], [-1, -1, 3], [1, -2, -4]]) # Матрица (левая часть системы)
v1 = numpy.array([1, -3, 5]) # Вектор (правая часть системы)
rez = numpy.linalg.solve(M1, v1)
print(f'x1 = {rez[0]}, x2 = {rez[1]}, x2 = {rez[2]}')
print('Задание №4')
def a(x : int):
    return numpy.sqrt(x) + (x*x)**(1/3)
v,err = integrate.quad(a, 0, 1)
print(v)

print('Задание №5')
def f(x, y):
    return (x - y) * math.exp(y)
v, err = integrate.dblquad(f, -1, 1, lambda y: 2*y, lambda y: y)
print(v)

print('Задание №6')
x = numpy.arange(-10, 10.01, 0.01)
plt.figure(figsize=(10, 5))
plt.plot(x, 3*numpy.sin(x), label=r'$f_1(x)=3*sin(x)$')
plt.plot(x, numpy.sqrt(5+x), label=r'$f_2(x)=√(5+x)$')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('figure_with_legend.png')
plt.show()