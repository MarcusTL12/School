import numpy as np
import matplotlib.pyplot as plt
import matplotlib2tikz.save as tikz_save


for i in range(-2, 3):
	plt.plot([np.log(5)], [np.arctan(-3 / 4) + 2 * np.pi * i], marker='o')

plt.grid(True)
plt.axis([-2, 2, -15, 15])
plt.xlabel("Re $z$")
plt.ylabel("Im $z$")

tikz_save("Oving8/Figurer/" + "f" + str(3) + ".tikz", figureheight='\\figureheight', figurewidth='\\figurewidth')
