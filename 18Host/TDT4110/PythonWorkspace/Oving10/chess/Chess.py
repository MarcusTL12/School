

pieces = [' ', '♖', '♜', '♘', '♞', '♗', '♝', '♕', '♛', '♔', '♚', '♙', '♟']


class Board:
	state = []

	def __init__(self):
		self.reset()
	
	
	def __str__(self):
		linesep = '   ' + '-' * 41 + '\n'
		linespace = '   |' * 9 + '\n'
		ret = ''
		for i in range(8):
			ret += linesep
			ret += ' ' + str(8 - i) + ' |'
			for j in range(8):
				ret += ' ' + pieces[self.state[i][j]] + '  |'
			ret += '\n'
		ret += linesep + ' '
		for i in range(8):
			ret += '    ' + chr(i + 65)
		return ret


	def reset(self):
		self.state = []
		self.state.append([1, 3, 5, 7, 9, 5, 3, 1])
		self.state.append([11 for i in range(8)])
		for i in range(4):
			self.state.append([0 for i in range(8)])
		self.state.append([12 for i in range(8)])
		self.state.append([2, 4, 6, 8, 10, 6, 4, 2])
	


def run():
	game = Board()

	print("hello")

	print(game)
