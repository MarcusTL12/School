import random as rnd
import ConsoleUtil as cu


def a():
	for i in range(1, 6):
		for j in range(1, i + 1):
			print(j, end=" ")
		print("")


def b_enklere():
	for i in range(5):
		print("#" + " " * i + " #")
	

def b():
	for i in range(5):
		print("# ", end="")
		for i in range(i):
			print(" ", end="")
		print("#")


def c():
	more_questions = True
	while more_questions:
		a = rnd.randint(0, 9)
		b = rnd.randint(0, 9)
		attempts = 3
		while attempts > 0:
			ans = input("Hva blir " + str(a) + " * " + str(b) + "? ")
			try:
				if int(ans) == a * b:
					print("Gratulerer, det ble helt riktig!")
					attempts = 0
				else:
					attempts -= 1
					print("Desverre ikke riktig. Du har " + str(attempts) + " forsøk igjen.")
			except:
				attempts -= 1
				print("Desverre ikke riktig. Du har " + str(attempts) + " forsøk igjen.")
		
		more = input("Er det ønskelig med flere spørsmål? Skriv 1 for ja og 0 for nei: ")
		more_questions = more != "0"


def d():
	more_questions = True
	difficulity = 1
	amt_correct = 0
	while more_questions:
		last_question_correct = False
		a = rnd.randint(0, 5 * difficulity)
		b = rnd.randint(0, 5 * difficulity)
		attempts = 3
		while attempts > 0:
			ans = input("Hva blir " + str(a) + " * " + str(b) + "? ")
			try:
				if int(ans) == a * b:
					print("Gratulerer, det ble helt riktig!")
					last_question_correct = True
					attempts = 0
				else:
					attempts -= 1
					print("Desverre ikke riktig. Du har " + str(attempts) + " forsøk igjen.")
			except:
				attempts -= 1
				print("Desverre ikke riktig. Du har " + str(attempts) + " forsøk igjen.")
		
		if last_question_correct:
			amt_correct += 1
		else:
			amt_correct = 0

		if amt_correct >= 5:
			amt_correct = 0
			difficulity += 1

		more = input("Er det ønskelig med flere spørsmål? Skriv 1 for ja og 0 for nei: ")
		more_questions = more != "0"
