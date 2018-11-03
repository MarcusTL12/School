

def bubblesort(l):
	for i in range(len(l) - 1):
		for j in range(len(l) - i - 1): 
			if l[j] > l[j + 1]:
				l[j], l[j + 1] = l[j + 1], l[j]


def selectionsort(l):
	for i in range(len(l)):
		minst = i
		for j in range(i, len(l)):
			if l[minst] > l[j]:
				minst = j
		l[minst], l[i] = l[i], l[minst]
		



def a():
	liste = [9, 1, 34, 7, 2, 3, 45, 6, 78, 56, 36, 65, 33, 21, 23, 34, 45, 6]
	print(liste)
	selectionsort(liste)
	print(liste)


'''
c)
Begge algorithmene har en asymptotisk tid på O(n^2), og når begge er implementert
som en "in-place" algorithme vil de bruke omtrent like mye minne også.
Selection sort vil skrive mye mindre til minne siden den kun bytter på to elementer
per gjennomløp av listen, hvor bubble sort bytter på alle den finner på veien som er i feil rekkefølge
'''
