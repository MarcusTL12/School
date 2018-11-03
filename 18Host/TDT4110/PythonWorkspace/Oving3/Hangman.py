import ConsoleUtil as cu


alphabet = "abcdefghijklmnopqrstuvwxyzæøå"
signs = ",.!:; "

def print_hang(word, guessed):
	won = True
	for i in range(len(word)):
		cur_char = word[i].lower()
		if cur_char in guessed or cur_char in signs:
			print(word[i], end="")
		else:
			print('_', end="")
			won = False
	print("")
	return won


def run():

	word = input("Hemmelig ord: ")

	valid_word = False

	while not valid_word:
		valid_word = True
		for i in word.lower():
			if i not in alphabet and i not in signs:
				valid_word = False
		
		if not valid_word:
			print("Ordet kan bare inneholde bokstaver og tegn; Prøv igjen:")
			word = input("Hemmelig ord: ")
	

	amt_lives = cu.cin_I("Antall liv: ")

	guessed_chars = []

	print_hang(word, guessed_chars)

	while amt_lives > 0:
		guess = ""
		guess_again = True
		while guess_again:
			guess_again = False
			guess = input("Gjett én bokstav: ")

			if len(guess) != 1:
				print("Gjett minst/bare én bokstav; Prøv igjen:")
				guess_again = True
			elif guess in guessed_chars:
				print("Du har allerede gjettet " + guess + "; Prøv igjen:")
				guess_again = True
			elif guess not in alphabet:
				print("Du kan bare gjette bokstaver; Prøv igjen:")
				guess_again = True

		correct_guess = guess.lower() in word.lower()

		if correct_guess:
			guessed_chars.append(guess)
			won = print_hang(word, guessed_chars)
			if won:
				print("Du vant!")
				return
		else:
			amt_lives -= 1
			print(guess + " er ikke i ordet; Du har nå " + str(amt_lives) + " liv igjen.")

	print("You Died!")
