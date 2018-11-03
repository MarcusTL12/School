import numpy as np

import matplotlib.pyplot as plt
import matplotlib2tikz.save as tikz_save

import copy



# def fourier(x, n):
# 	ret = 0
# 	sgn = 1
# 	for i in range(n):
# 		k = i + 1
# 		if k % 2 == 0:
# 			pass
# 		else:
# 			ret += (4 / (np.pi * k)) * np.sin(k * x)
# 	return ret


# def q(x):
# 	return -2 * np.cos(x) + 2 / 75 * np.cos(3 * x) + 8 / 225 * np.sin(3 * x)


def f(x):
	return 1 / 2 if x < 2 else 0

def F(x):
	return x / 2 if x < 2 else 1


y = np.vectorize(f)
y1 = np.vectorize(F)

x = np.arange(0, 3, 0.01)

for i in range(1):
	plt.clf()
	plt.plot(x, y(x), 'black')
	plt.plot(x, y1(x), 'black')
	plt.axis([0, 3, 0, 1.5])
	plt.grid(True)
	# plt.title(r"$F_{" + str(i * 2) + "} (x)$")
	plt.title("$f(x), F(x), \\theta = 2$")
	tikz_save("Oving2/Figurer/" + "f" + str(3) + ".tikz", figureheight='\\figureheight', figurewidth='\\figurewidth')


plt.savefig("Python/plot.png")
