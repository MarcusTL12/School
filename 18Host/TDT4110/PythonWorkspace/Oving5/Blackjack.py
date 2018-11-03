import random


def shuffle(cards):
	for i in range(len(cards)):
		randindex = random.randrange(0, len(cards))
		cards[randindex], cards[i] = cards[i], cards[randindex]


def run():
	stack = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'A'] * 4

	shuffle(stack)

	stack_top = 51

	dealer_cards = []

	your_cards = []

	dealer_cards.append(stack[stack_top])
	stack_top -= 2
	your_cards.append(stack[stack_top])
	stack_top -= 2
	dealer_cards.append(stack[stack_top])
	stack_top -= 2
	your_cards.append(stack[stack_top])
	stack_top -= 2

	print("Dealers cards are " + str(dealer_cards[0]) + " and ?")
	
	done = False

	ace_value = 11
	ace_set = 'A' in your_cards
	score = 0
	dealers_score = 0
	for i in your_cards:
		score += i if i != 'A' else ace_value
	for i in dealer_cards:
		dealers_score += i if i != 'A' else ace_value



	while not done:
		print("Your score is " + str(score))
		done = input("Do you want andother card? (Y/N) ").lower() == 'n'
		if not done:
			new_card = stack[stack_top]
			stack_top -= 2
			your_cards.append(new_card)
			score += i if i != 'A' else ace_value
			if new_card == 'A' and not ace_set:
				ace_set = True
				if score > 21:
					score -= 10
					ace_value = 1
			
			if score >= 21:
				done = True
	
	if score > 21:
		print("You got " + str(score))
		print("You lost!")
	else:
		print("Dealers score is: " + str(dealers_score))
		print("You " + ("won!" if score >= dealers_score else "lost!"))


