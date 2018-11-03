import numpy as np
import matplotlib.pyplot as plt
import matplotlib2tikz.save as tikz_save
import shapely.geometry as sg
import descartes

a = sg.Point(0, 0).buffer(0.5**2)

b = sg.Polygon([(0, 0), (1, np.tan(np.pi / 4)), (1, -np.tan(np.pi / 4))])

ax = plt.gca()
ax.add_patch(descartes.PolygonPatch(a.intersection(b), fc='#7f7f7f', ec='k', alpha=1))
# ax.add_patch(descartes.PolygonPatch(b, fc='#ff00ff', ec='k', alpha=1))


ax.set_xlim(-0.75, 0.75)
ax.set_ylim(-0.75, 0.75)
ax.set_aspect('equal')

plt.title("w plane")
plt.xlabel("Re z")
plt.ylabel("Im z")
plt.grid(True)

tikz_save("Oving9/Figurer/" + "f" + str(3) + ".tikz", figureheight='\\figureheight', figurewidth='\\figurewidth')

# plt.show()


