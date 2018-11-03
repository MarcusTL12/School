import numpy as np
import matplotlib.pyplot as plt
import math


def makeMO(energy, x_min, x_max):
	plt.plot([x_min, x_max], [energy, energy], 'k')


def makemultiMO(energy, x_start, amt):
	if amt == 1:
		makeMO(energy, x_start, x_start + 1)
		return

	space = 0.05

	makeMO(energy, x_start, x_start + 1 / amt - space)
	for i in range(1, amt - 1):
		makeMO(energy, x_start + i / amt + space, x_start + (i + 1) / amt - space)
	
	makeMO(energy, x_start + (amt - 1) / amt + space, x_start + 1)


tol = 0.01


def makeMOdiagram(energies, x_start):
	i = 0
	while i < len(energies):
		count = 1
		j = i + 1
		while j < len(energies) and abs(energies[i] - energies[j]) < tol:
			count += 1
			j += 1
		
		makemultiMO(energies[i], x_start, count)

		i += count


energies1 = [
	-18.39369,
	-12.82480,
	-12.82480,
	6.46988,
	19.75746,
	21.17196,
	21.17196
]


energies2 = [
	-18.00499,
	-11.87384,
	-11.87368,
	5.24497,
	19.05362,
	19.05399,
	22.01015
]


energies3 = [
	-18.11788,
	-10.42134,
	-10.42134,
	3.79684,
	17.4938,
	17.4938,
	26.59889
]

# with plt.xkcd():
makeMOdiagram(energies1, 1)
makeMOdiagram(energies2, 3)
makeMOdiagram(energies3, 5)

plt.show()
