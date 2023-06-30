from game.domain.models import Board


class Game:
    def __init__(self, base: Board) -> None:
        self.whites = 0
        self.blacks = 0
        self.w_queens = 0
        self.b_queens = 0
        self.turn = False
        self.board = [[0] * 8 for _ in range(8)]
        self.winner = -1
        self.emp = 0
        self.history = []

        for piece in base.get_player_pieces():
            if piece.get_is_queen():
                current_piece = 3
                self.w_queens += 1
            else:
                current_piece = 1
            self.board[piece.get_x_coordinate()][piece.get_y_coordinate()] = current_piece
            self.whites += 1

        for piece in base.get_ai_pieces():
            if piece.get_is_queen():
                current_piece = 4
                self.b_queens += 1
            else:
                current_piece = 2
            self.board[piece.get_x_coordinate()][piece.get_y_coordinate()] = current_piece
            self.blacks += 1

        self.moves = self.possible_moves()
        self.takes = self.possible_takes()

    def check_winner(self):
        if self.moves == [] and self.takes == []:
            if self.emp >= 40:
                return 0
            if self.blacks == 0:
                return 1
            if self.whites == 0:
                return 2
            return 0
        return -1

    def get_state(self):
        r = self.check_winner()
        if r == 1:
            return float('inf')
        if r == 2:
            return float('-inf')
        if r == 0:
            return 0
        return (self.whites + (4 * self.w_queens)) - (self.blacks + (4 * self.b_queens))

    def possible_takes(self, col=-1, row=-1):
        takes = []
        enemies = []
        if self.turn:
            enemies = [2, 4]
            allies = [1, 3]
        else:
            enemies = [1, 3]
            allies = [2, 4]

        def check_takes(x: int, y: int):
            piece = self.board[x][y]
            if (piece in [3, 4] or self.turn) and piece in allies:
                if x - 2 >= 0 and y - 2 >= 0 and self.board[x - 1][y - 1] in enemies and self.board[x - 2][y - 2] == 0:
                    takes.append([x, y, x - 2, y - 2])
                if x + 2 < 8 and y - 2 >= 0 and self.board[x + 1][y - 1] in enemies and self.board[x + 2][y - 2] == 0:
                    takes.append([x, y, x + 2, y - 2])
            if (piece in [3, 4] or not self.turn) and self.board[x][y] in allies:
                if x - 2 >= 0 and y + 2 < 8 and self.board[x - 1][y + 1] in enemies and self.board[x - 2][y + 2] == 0:
                    takes.append([x, y, x - 2, y + 2])
                if x + 2 < 8 and y + 2 < 8 and self.board[x + 1][y + 1] in enemies and self.board[x + 2][y + 2] == 0:
                    takes.append([x, y, x + 2, y + 2])

        if col == -1:
            for row in range(8):
                for col in range(8):
                    check_takes(col, row)
        else:
            check_takes(col, row)

        multi_takes = list()
        for take in takes:
            self.play(take, 0, 1)
            new_takes = self.possible_takes(take[2], take[3])
            for new_take in new_takes:
                multi_takes.append(take + [new_take[2], new_take[3]])
            self.undo(True)
        final = multi_takes + takes
        return final

    def possible_moves(self):
        moves = []
        allies = []
        if self.turn:
            allies = [1, 3]
        else:
            allies = [2, 4]

        for row in range(8):
            for col in range(8):
                piece = self.board[col][row]
                if (piece in [3, 4] or self.turn) and piece in allies:
                    if col - 1 >= 0 and row - 1 >= 0:
                        if self.board[col - 1][row - 1] == 0:
                            moves.append([col, row, col - 1, row - 1])
                    if col + 1 < 8 and row - 1 >= 0:
                        if self.board[col + 1][row - 1] == 0:
                            moves.append([col, row, col + 1, row - 1])
                if (piece in [3, 4] or not self.turn) and self.board[col][row] in allies:
                    if col - 1 >= 0 and row + 1 < 8:
                        if self.board[col - 1][row + 1] == 0:
                            moves.append([col, row, col - 1, row + 1])
                    if col + 1 < 8 and row + 1 < 8:
                        if self.board[col + 1][row + 1] == 0:
                            moves.append([col, row, col + 1, row + 1])
        return moves

    def undo(self, override=False):
        current_move = self.history[-1]

        def recur(action: list):
            self.board[action[0]][action[1]], self.board[action[2]][action[3]] = \
                self.board[action[2]][action[3]], self.board[action[0]][action[1]]

            if action[4] != 0:
                self.board[(action[2] + action[0]) // 2][(action[1] + action[3]) // 2] = action[4]
                if action[4] % 2 == 1:
                    self.whites += 1
                else:
                    self.blacks += 1

            if action[5]:
                self.board[action[0]][action[1]] -= 2
                if self.board[action[0]][action[1]] == 1:
                    self.w_queens -= 1
                else:
                    self.b_queens -= 1

        if type(current_move[0]) == list:
            for move in reversed(current_move):
                recur(move)
        else:
            recur(current_move)
        self.winner = -1

        if not override:
            self.turn = not self.turn
            self.moves = self.possible_moves()
            self.takes = self.possible_takes()

        self.history.pop()

    def play(self, move, prof=0, override=0):
        if prof > 0:
            self.takes = self.possible_takes()
            self.moves = self.possible_moves()
        valid = False
        took = 0
        queen = False
        if override == 1 or (move in self.takes):
            self.board[move[0]][move[1]], self.board[move[2]][move[3]] = \
                self.board[move[2]][move[3]], self.board[move[0]][move[1]]
            self.board[(move[2] + move[0]) // 2][(move[1] + move[3]) // 2], took = \
                took, self.board[(move[2] + move[0]) // 2][(move[1] + move[3]) // 2]

            if self.turn:
                self.blacks -= 1
            else:
                self.whites -= 1

            valid = True
            if override == 0:
                self.emp = 0

        elif len(self.takes) == 0 and move in self.moves:
            self.board[move[0]][move[1]], self.board[move[2]][move[3]] = self.board[move[2]][move[3]], \
                self.board[move[0]][move[1]]
            valid = True
            if override == 0:
                self.emp += 1
        if valid:
            if self.board[move[2]][move[3]] == 1 and move[3] == 0:
                self.board[move[2]][move[3]] = 3
                self.w_queens += 1
                queen = True
            elif self.board[move[2]][move[3]] == 2 and move[3] == 7:
                self.board[move[2]][move[3]] = 4
                self.b_queens += 1
                queen = True
            this_play = move[:4]
            this_play += [took, queen]
            if len(move) > 4:
                move = move[2:]
                if prof == 0:
                    this_play = [this_play]
                this_play.append(self.play(move, prof + 1, override))
        if prof > 0:
            return this_play
        if valid:
            self.history.append(this_play)
        return valid

    def get_board(self) -> Board:
        matrix = [[0] * 8 for _ in range(8)]
        for y in range(8):
            for x in range(8):
                matrix[y][x] = self.board[x][y]
        return Board(matrix)
