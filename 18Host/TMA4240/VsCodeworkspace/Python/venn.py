import numpy as np
import matplotlib.pyplot as plt
import matplotlib2tikz.save as tikz_save
import shapely.geometry as sg
import descartes


# create the circles with shapely
a = sg.Point(0, np.sqrt(3) / 2).buffer(1.0)
b = sg.Point(-.5, 0).buffer(1.0)
c = sg.Point(0.5, 0).buffer(1.0)

# compute the 3 parts
a_ = a.difference(b.union(c))
b_ = b.difference(a.union(c))
c_ = c.difference(a.union(b))
ab = a.intersection(b).difference(c)
bc = b.intersection(c).difference(a)
ca = c.intersection(a).difference(b)
abc = a.intersection(b.intersection(c))

# use descartes to create the matplotlib patches
ax = plt.gca()
ax.add_patch(descartes.PolygonPatch(a_, fc='#FFFFFF', ec='k', alpha=1))
ax.add_patch(descartes.PolygonPatch(b_, fc='#FFFFFF', ec='k', alpha=1))
ax.add_patch(descartes.PolygonPatch(c_, fc='#FFFFFF', ec='k', alpha=1))
ax.add_patch(descartes.PolygonPatch(ab, fc='#7F7F7F', ec='k', alpha=1))
ax.add_patch(descartes.PolygonPatch(bc, fc='#FFFFFF', ec='k', alpha=1))
ax.add_patch(descartes.PolygonPatch(ca, fc='#7F7F7F', ec='k', alpha=1))
ax.add_patch(descartes.PolygonPatch(abc, fc='#7F7F7F', ec='k', alpha=1))

# control display

plt.text(-0.3, 1.25, "A", fontsize=42)
plt.text(-1.3, -0.25, "B", fontsize=42)
plt.text(0.8, -0.25, "C", fontsize=42)

plt.box(False)
plt.axis('off')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')

tikz_save("Oving2/Figurer/" + "f" + str(2) + ".tikz", figureheight='\\figureheight', figurewidth='\\figurewidth')
plt.savefig("Python/venn.png")

