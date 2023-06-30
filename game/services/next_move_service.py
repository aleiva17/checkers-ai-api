from shared.domain.models import singleton
from game.domain.models import Game
from game.services import MinimaxService


@singleton
class NextMoveService:
    def __init__(self, minimax_service: MinimaxService):
        self.__minimax_service: MinimaxService = minimax_service

    def make_ai_move(self, game: Game):
        _, move = self.__minimax_service.minimax(game)
        game.play(move)
        return game.get_board()
