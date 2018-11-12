import numpy as np
import matplotlib.pyplot as plt
import matplotlib2tikz.save as tikz_save
import cmath


def make_arrow(f, t):
	plt.arrow(f(t).real, f(t).imag, f(t + 0.01).real - f(t).real, f(t + 0.01).imag - f(t).imag, shape='full', lw=0, length_includes_head=True, head_width=.1)


def f(t):
	return 1 + 1j + np.e**(- np.pi * 1j * t)


plt.plot(-1, 2, marker='o', color='k')
plt.plot(1, 4, marker='o', color='k')

plt.plot([-1, 1], [2, 4], color='k')

plt.arrow(0, 3, 0.01, 0.01, shape='full', lw=0, length_includes_head=True, head_width=.1, color='k')

plt.grid(True)
plt.axis([-2, 2, 1, 5])
plt.xlabel("Re $z$")
plt.ylabel("Im $z$")

tikz_save("Oving9/Figurer/" + "f" + str(1) + ".tikz", figureheight='\\figureheight', figurewidth='\\figurewidth')

# plt.show()

