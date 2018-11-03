

def to_cash(x):
	twenties = x // 20
	tens = (x % 20) // 10
	fives = (x % 10) // 5
	ones = x % 5

	return [twenties, tens, fives, ones]


def run():
	teeth = [95, 103, 71, 99, 114, 64, 95, 53, 97, 114, 109, 11, 2, 21, 45, 2, 26, 81, 54, 14, 118, 108, 117, 27, 115, 43, 70, 58, 107]

	for i in teeth:
		cash = to_cash(i)
		print("20: " + str(cash[0]).rjust(3) + ", 10: " + str(cash[1]) + ", 5: " + str(cash[2]) + ", 1: " + str(cash[3]))