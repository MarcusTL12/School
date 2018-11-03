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




def f(x, t, n):
	ret = 0
	sgn = 1
	for i in range(1, n + 1, 2):
		ret += sgn / (i**3) * np.sin(i * t) * np.sin(i * x)
		sgn *= -1
	
	return 0.01 * (4 / np.pi) * ret



y = np.vectorize(f)

x = np.arange(0, np.pi, 0.001)

for i in range(9):
	plt.clf()
	plt.plot(x, y(x, i * np.pi / 8, 625), 'k')
	plt.axis([0, np.pi, -0.02, 0.02])
	plt.grid(True)
	# plt.title(r"$F_{" + str(i * 2) + "} (x)$")
	plt.title(r"$u(x, " + format(i * np.pi / 8, '.2f') + ")$")
	tikz_save("Oving6/Figurer/" + "h" + str(i) + ".tikz", figureheight='\\figureheight', figurewidth='\\figurewidth')


plt.savefig("Python/plot.png")
