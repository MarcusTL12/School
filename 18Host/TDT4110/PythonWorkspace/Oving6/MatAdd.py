import random


def random_matrise(w, h):
	res = [[]] * h
	for i in range(h):
		res[i] = [0] * w
		for j in range(w):
			res[i][j] = random.randint(0, 10)
	return res


def print_matrise(mat, name):
	print(name + " = [")
	for i in mat:
		print(" " * (len(name) + 3) + " " + str(i))
	print(" " * (len(name) + 3) + "]")


def matrise_addisjon(a, b):
	if len(a) != len(b) or len(a[0]) != len(b[0]):
		print("Matrisene er ikke av samme dimensjon")
		return
	
	res = [[]] * len(a)
	
	for i in range(len(a)):
		res[i] = [0] * len(a[0])
		for j in range(len(a[0])):
			res[i][j] = a[i][j] + b[i][j]
	return res


def main():
    A = random_matrise(4,3)
    print_matrise(A, 'A')
    B = random_matrise(3,4)
    print_matrise(B, 'B')
    C = random_matrise(3,4)
    print_matrise(C, 'C')
    D = matrise_addisjon(A,B)
    E = matrise_addisjon(B,C)
    print_matrise(E, 'B+C' )