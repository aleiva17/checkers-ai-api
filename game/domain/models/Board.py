from game.domain.models import Piece


class Board:
    def __init__(self, board: list[list] = None):
        self.__player_pieces: list[Piece] = []
        self.__ai_pieces: list[Piece] = []

        if board:
            for y in range(8):
                for x in range(8):
                    piece = board[x][y]
                    if piece in (1, 3):
                        self.__player_pieces.append(Piece(piece > 2, y, x))
                    elif piece in (2, 4):
                        self.__ai_pieces.append(Piece(piece > 2, y, x))

    def set_player_pieces(self, pieces: list[Piece]):
        self.__player_pieces = pieces

    def set_ai_pieces(self, pieces: list[Piece]):
        self.__ai_pieces = pieces

    def get_player_pieces(self) -> list[Piece]:
        return self.__player_pieces

    def get_ai_pieces(self) -> list[Piece]:
        return self.__ai_pieces
