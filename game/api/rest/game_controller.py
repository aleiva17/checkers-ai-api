from fastapi import APIRouter, Depends
from game.resources import BoardResource
from game.domain.models import Board, Game
from game.services import MinimaxService, NextMoveService
from shared.mapping import mapper as mapper_singleton

game_controller = APIRouter()


@game_controller.post("/api/v1/game/next-move")
def next_move(resource: BoardResource, mapper=Depends(lambda: mapper_singleton)) -> BoardResource:
    """
    Retrieve the next move for a game. It accepts a JSON payload containing the current game board information in the BoardResource format.
    Upon successful execution, the endpoint returns the updated BoardResource representing the game board after the next move has been made.
    This interactive documentation provides comprehensive details about the request parameters and the expected response format.
    """
    board: Board = mapper.map(resource, Board)

    game = Game(board)
    minimax_service = MinimaxService()
    next_move_service = NextMoveService(minimax_service)
    next_move_service.make_ai_move(game)

    board_resource: BoardResource = mapper.map(game.get_board(), BoardResource)
    return board_resource
