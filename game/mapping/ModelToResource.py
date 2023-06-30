from game.domain.models import Board, Piece
from game.resources import BoardResource, PieceResource


class ModelToResource:
    @staticmethod
    def piece_to_piece_resource(model: Piece) -> PieceResource:
        resource = PieceResource(
            is_queen=model.get_is_queen(),
            y_coordinate=model.get_y_coordinate(),
            x_coordinate=model.get_x_coordinate()
        )
        return resource

    @staticmethod
    def board_to_board_resource(model: Board) -> BoardResource:
        resource = BoardResource(
            ai_pieces=[ModelToResource.piece_to_piece_resource(piece) for piece in model.get_ai_pieces()],
            player_pieces=[ModelToResource.piece_to_piece_resource(piece) for piece in model.get_player_pieces()]
        )
        return resource
