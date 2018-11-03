from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# import matplotlib2tikz.save as tikz_save



def plot_implicit(fn, bbox=(-2.5, 2.5)):
	''' create a plot of an implicit function
	fn  ...implicit function (plot where fn==0)
	bbox ..the x,y,and z limits of plotted interval'''
	xmin, xmax, ymin, ymax, zmin, zmax = bbox * 3
	ax = plt.axes(projection='3d')
	A = np.linspace(xmin, xmax, 200) # resolution of the contour
	B = np.linspace(xmin, xmax, 30) # number of slices
	A1, A2 = np.meshgrid(A, A) # grid on which the contour is plotted

	# colmap = plt.cm.get_cmap("winter")
	# colmap.set_under("magenta")
	# colmap.set_over("yellow")

	for z in B: # plot contours in the XY plane
		X, Y = A1, A2
		Z = fn(X, Y, z)
		cset = plt.contour(X, Y, Z + z, [z], zdir='z', linestyles='solid', colors=[[(1 * z - bbox[0]) / (bbox[1] - bbox[0]), 0.3, (1 * z - bbox[0]) / (bbox[1] - bbox[0])]])
		cset.cmap.set_under('yellow')
		cset.cmap.set_over('cyan')
		# [z] defines the only level to plot for this contour for this value of z

	for y in B: # plot contours in the XZ plane
		X, Z = A1, A2
		Y = fn(X, y, Z)
		cset = plt.contour(X, Y + y, Z, [y], zdir='y', linestyles='solid', colors=[[(1 * y - bbox[0]) / (bbox[1] - bbox[0]), 0.3, (1 * y - bbox[0]) / (bbox[1] - bbox[0])]])

	for x in B: # plot contours in the YZ plane
		Y, Z = A1, A2
		X = fn(x, Y, Z)
		cset = plt.contour(X + x, Y, Z, [x], zdir='x', linestyles='solid', colors=[[(1 * x - bbox[0]) / (bbox[1] - bbox[0]), 0.3, (1 * x - bbox[0]) / (bbox[1] - bbox[0])]])

	# must set plot limits because the contour will likely extend
	# way beyond the displayed level.  Otherwise matplotlib extends the plot limits
	# to encompass all values in the contour.
	ax.set_zlim3d(zmin, zmax)
	ax.set_xlim3d(xmin, xmax)
	ax.set_ylim3d(ymin, ymax)


# def f(x, y, z):
# 	a, b, c = 0.0, -5.0, 11.8
# 	return x**4 + y**4 + z**4 + a * (x**2 + y**2 + z**2)**2 + b * (x**2 + y**2 + z**2) + c


def r(x, y, z):
	return np.sqrt(x**2 + y**2 + z**2)


def sP(x, y, z):
	return 1 / np.sqrt(2)


def sF(x, y, z):
	return 1 / np.sqrt(2 * np.pi)


def s1R(x, y, z):
	return 2 * np.exp(-r(x, y, z))


def s2R(x, y, z):
	return (1 / (2 * np.sqrt(2))) * (2 - r(x, y, z)) * np.exp(-r(x, y, z) / 2)


def s1(x, y, z):
	return s1R(x, y, z) * sP(x, y, z) * sF(x, y, z)


def s2(x, y, z):
	return s2R(x, y, z) * sP(x, y, z) * sF(x, y, z)


def f(x, y, z):
	return s1(x, y, z)**2 - 0.032


plot_implicit(f, (-5, 5))


# tikz_save("PyPlotTesting/Figurer/" + "f" + str(1) + ".tikz", figureheight='\\figureheight', figurewidth='\\figurewidth')

plt.savefig("PyPlotTesting/Figurer/test.png")

plt.show()
