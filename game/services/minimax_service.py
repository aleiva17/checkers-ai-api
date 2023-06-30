from shared.domain.models import singleton
from game.domain.models import Game


@singleton
class MinimaxService:
    def __init__(self):
        self.__max_depth = 5

    def minimax(self, game: Game, depth: int = 0, alfa=float('-inf'), beta=float('inf')):
        best_move = [0, 0, 0, 0]
        if depth > self.__max_depth or game.winner != -1:
            return game.get_state(), [0, 0, 0, 0]
        plays = game.takes
        if not plays:
            plays = game.moves
        if game.turn:
            value = float('-inf')
            for move in plays:
                ok = game.play(move, 0, 2)
                if ok:
                    game.turn = not game.turn
                    game.takes = game.possible_takes()
                    game.moves = game.possible_moves()
                    game.winner = game.check_winner()
                    res, _ = self.minimax(game, depth + 1, alfa, beta)
                    if res >= value:
                        best_move = move
                        value = res
                    alfa = max(alfa, value)
                    game.undo()
                    if beta <= alfa:
                        break
            return value, best_move
        else:
            value = float('inf')
            for move in plays:
                ok = game.play(move, 0, 2)
                if ok:
                    game.turn = not game.turn
                    game.takes = game.possible_takes()
                    game.moves = game.possible_moves()
                    game.winner = game.check_winner()
                    res, _ = self.minimax(game, depth + 1, alfa, beta)
                    if res <= value:
                        best_move = move
                        value = res
                    beta = max(beta, value)
                    game.undo()
                    if beta <= alfa:
                        break
            return value, best_move
