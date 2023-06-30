from game.domain.models import Board, Piece
from game.resources import BoardResource, PieceResource


class ResourceToModel:
    @staticmethod
    def piece_resource_to_piece(resource: PieceResource) -> Piece:
        model = Piece()

        model.set_coordinates(resource.x_coordinate, resource.y_coordinate)
        model.set_is_queen(resource.is_queen)

        return model

    @staticmethod
    def board_resource_to_board(resource: BoardResource) -> Board:
        model = Board()

        model.set_ai_pieces([ResourceToModel.piece_resource_to_piece(piece) for piece in resource.ai_pieces])
        model.set_player_pieces([ResourceToModel.piece_resource_to_piece(piece) for piece in resource.player_pieces])

        return model
