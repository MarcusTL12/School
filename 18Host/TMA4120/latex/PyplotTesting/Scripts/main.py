import numpy as np
import matplotlib.pyplot as plt
import matplotlib2tikz.save as tikz_save
import math



def derivative(y, h, n: int=1):
	if n == 1:
		return lambda x: (y(x + h) - y(x - h)) / (2 * h)
	else:
		return derivative(derivative(y, h, n - 1), h, 1)


def integral(y, h, a, b):
	ret = 0

	sgn = 1

	if a > b:
		sgn = -1
		a, b = b, a

	if abs(b - a) < h:
		h *= abs(b - a)

	for i in np.arange(a, b, h):
		ret += y(i) * h

	return ret * sgn


def fourier(y, h, n, a, b):
	L = (b - a) / 2
	a_0 = integral(y, h, a, b) / (2 * L)
	a_n = [0] * n
	b_n = [0] * n
	for i in range(1, n + 1):
		a_n[i - 1] = (1 / L) * integral(lambda x: y(x) * np.cos(i * np.pi * x / L), h, a, b)
		b_n[i - 1] = (1 / L) * integral(lambda x: y(x) * np.sin(i * np.pi * x / L), h, a, b)

	return lambda x: fouriereval(x, a_0, a_n, b_n, L)


def fouriereval(x, a_0, a_n, b_n, l):
	ret = a_0

	for i in range(1, len(a_n) + 1):
		ret += a_n[i - 1] * np.cos(i * np.pi * x / l)
		ret += b_n[i - 1] * np.sin(i * np.pi * x / l)

	return ret


# def f(x):
# 	if x > 2:
# 		return f(x - 4)
# 	if x < -2:
# 		return f(x + 4)
# 	return ((x**3) - 4 * x) / 4


# def f(x):
# 	if x < -1:
# 		return f(x + 2)
# 	if x > 1:
# 		return f(x - 2)
# 	return -1 if x < 0 else 1


def fx(x, n):
	if n == 1:
		return np.sin(x)
	return fx(np.sin(x) * np.pi / 2, n - 1)

# def f(x):
# 	return np.cos(np.tan(np.sin(x)))


def sirc(x):
	return np.sqrt(1 - x**2)


def f(x):
	if x < -2:
		return f(x + 4)
	if x > 2:
		return f(x - 4)
	if x < 0:
		return -sirc(x + 1)
	else:
		return sirc(x - 1)


h = 0.001

x = np.arange(-4, 4, 0.01)

# kr = lambda x: derivative(f, h, 2)(x) / ((1 + derivative(f, h)(x)**2)**(3 / 2))

# dkr = derivative(kr, h)

# dy = derivative(f, h)

fr = fourier(f, h, 101, -2, 2)

plt.plot(x, np.vectorize(f)(x))
# plt.plot(x, np.vectorize(kr)(x))
# plt.plot(x, np.vectorize(dkr)(x))
# plt.plot(x, np.vectorize(dy)(x))
plt.plot(x, np.vectorize(fr)(x))

plt.axis([-4, 4, -5, 5])

plt.title("$f(x)$")

plt.grid(True)

tikz_save("PyPlotTesting/Figurer/" + "f" + str(1) + ".tikz", figureheight='\\figureheight', figurewidth='\\figurewidth')
