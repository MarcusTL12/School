

class Board:
    state = []

    all_moves = []

    undo_stack = []

    def __init__(self):
        self.reset()

    def __str__(self):
        pieces = [' ', '♖', '♜', '♘', '♞', '♗', '♝', '♕', '♛', '♔', '♚', '♙', '♟']
        linesep = '   ' + '-' * 41 + '\n'
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
        return ret + '\n'

    def reset(self):
        self.state = []
        self.state.append([1, 3, 5, 7, 9, 5, 3, 1])
        self.state.append([11 for i in range(8)])
        for i in range(4):
            self.state.append([0 for i in range(8)])
        self.state.append([12 for i in range(8)])
        self.state.append([2, 4, 6, 8, 10, 6, 4, 2])

    def getPiece(self, pos):
        return self.state[pos[1]][pos[0]]

    def setPiece(self, pos, val):
        self.state[pos[1]][pos[0]] = val

    def is_same_col(self, pos1, pos2, opp=False):
        return (self.getPiece(pos1) + self.getPiece(pos2)) % 2 == (1 if opp else 0) and (0 not in (self.getPiece(pos1), self.getPiece(pos2)))

    def make_move(self, move):
        self.undo_stack.append(
            (move, (self.getPiece(move[0]), self.getPiece(move[1]))))
        self.setPiece(move[1], self.getPiece(move[0]))
        self.setPiece(move[0], 0)
        if ((self.getPiece(move[1]) - 1) // 2) == 5 and (move[1][1] + self.getPiece(move[1])) % 2 == 0 and move[1][1] in [0, 7]:
            self.setPiece(move[1], 8 - self.getPiece(move[1]) % 2)

    def undo_move(self):
        move = self.undo_stack.pop()
        self.setPiece(move[0][0], move[1][0])
        self.setPiece(move[0][1], move[1][1])

    def valid_piece_moves(self, pos):
        moves = []
        piece = self.getPiece(pos)
        if piece == 0:
            return moves
        if (piece - 1) // 2 in [0, 2, 3, 4]:
            dirs = []
            if (piece - 1) // 2 in [0, 3, 4]:
                dirs.extend([(1, 0), (0, 1), (-1, 0), (0, -1)])
            if (piece - 1) // 2 in [2, 3, 4]:
                dirs.extend([(1, 1), (-1, 1), (-1, -1), (1, -1)])
            for xm, ym in dirs:
                x, y = pos
                while True:
                    x += xm
                    y += ym
                    if not inbounds((x, y)):
                        break
                    if self.is_same_col(pos, (x, y)):
                        break
                    elif self.is_same_col(pos, (x, y), True):
                        moves.append((x, y))
                        break
                    moves.append((x, y))
                    if (piece - 1) // 2 == 4:
                        break
        if (piece - 1) // 2 == 1:
            dirs = ((2, 1), (1, 2), (-1, 2), (-2, 1),
                    (-2, -1), (-1, -2), (1, -2), (2, -1))
            for xm, ym in dirs:
                x, y = pos
                x += xm
                y += ym
                if inbounds((x, y)) and not self.is_same_col(pos, (x, y)):
                    moves.append((x, y))
        if (piece - 1) // 2 == 5:
            x, y = pos
            unit_mov = -1 + 2 * (self.getPiece(pos) % 2)
            dbl_mov = y == 1 and self.getPiece(
                pos) % 2 == 1 or y == 6 and self.getPiece(pos) % 2 == 0
            dirs = [(0, unit_mov)]
            if dbl_mov:
                dirs.append((0, 2 * unit_mov))
            for i in (-1, 1):
                if inbounds((x + i, y + unit_mov)) and self.is_same_col(pos, (x + i, y + unit_mov), True):
                    moves.append((x + i, y + unit_mov))
            for xm, ym in dirs:
                x, y = pos
                x += xm
                y += ym
                if inbounds((x, y)) and self.getPiece((x, y)) == 0:
                    moves.append((x, y))
        return moves

    def all_valid_moves(self, turn):
        entries = []
        exits = []
        for y in range(8):
            for x in range(8):
                if self.getPiece((x, y)) % 2 == (1 if turn else 0) and self.getPiece((x, y)) != 0:
                    temp = self.valid_piece_moves((x, y))
                    entries.extend([(x, y)] * len(temp))
                    exits.extend(temp)
        return (entries, exits)

    def update_valid_moves(self, turn):
        check_moves = []
        movs = self.all_valid_moves(turn)
        for i in zip(movs[0], movs[1]):
            self.make_move(i)
            self.all_moves = self.all_valid_moves(not turn)
            if self.check(not turn):
                check_moves.append(i)
            self.undo_move()
        self.all_moves = ([j[0] for j in zip(movs[0], movs[1]) if j not in check_moves], [j[1] for j in zip(movs[0], movs[1]) if j not in check_moves])

    def find_king(self, turn):
        for y in range(8):
            for x in range(8):
                if (self.getPiece((x, y)) - (1 if turn else 0)) == 9:
                    return x, y

    def check(self, turn):
        movs = self.all_valid_moves(turn)
        return self.find_king(turn) in movs[1]


def inbounds(pos):
    return pos[0] >= 0 and pos[0] < 8 and pos[1] >= 0 and pos[1] < 8


def to_pos(pos_str):
    if len(pos_str) != 2:
        return (-1, -1)
    pos = (ord(pos_str[0]) - 65, 8 - int(pos_str[1]))
    if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7:
        return (-1, -1)
    return pos


def prompt_move(game):
    valid_move = False
    message = "Make a move (ex. a2 a4): "
    ret = (0, 0)
    while not valid_move:
        inp = input(message).upper().split(' ')
        if len(inp) != 2:
            message = "Not valid move, Try again: "
            continue
        ret = (to_pos(inp[0]), to_pos(inp[1]))
        if ret not in zip(game.all_moves[0], game.all_moves[1]):
            print("Not valid move, Try again: ")
            continue
        valid_move = True
    return ret


def run():
    game = Board()
    turn = True
    game.update_valid_moves(not turn)
    while True:
        print(game)
        print("Number of possible moves:", len(game.all_moves[0]))
        mov = prompt_move(game)
        game.make_move(mov)
        game.update_valid_moves(turn)
        if len(game.all_moves[0]) == 0:
            print("checkmate!")
            break
        elif game.check(not turn):
            print("check!")
        turn = not turn
