import math


def f(x):
	return (x - 12) * math.exp(5 * x) - 8 * (x + 2) ** 2


def g(x):
	return - x - 2 * x ** 2 - 5 * x ** 3 + 6 * x ** 4


def f_1(x):
	return (x ** 3 - 3 * x + 2) ** 2


def derivative_at(h, x, func):
	return (func(x + h / 2) - func(x - h / 2)) / h


def derivative(h, func):
	return lambda x : (func(x + h / 2) - func(x - h / 2)) / h


def secant_method(h, x, func, tol):
	if derivative_at(h, x, func) == 0:
		return secant_method(h, x + 1, func, tol)
	iterations = 0
	while func(x - tol) * func(x + tol) > 0:
		if iterations > 20 or derivative_at(h, x, func) == 0:
			return secant_method(h, x, derivative(h, func), tol)
		x -= func(x) / derivative_at(h, x, func)
		iterations += 1
	return x


def a():
	print(f(0))
	print(g(1))


def b():
	print(derivative_at(0.000001, -2, f))


def c():
	x_1 = secant_method(0.00000001, -1.5, f_1, 0.0000000001)
	print((x_1, f_1(x_1)))

