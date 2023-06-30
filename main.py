from fastapi import FastAPI
from game.api.rest.game_controller import game_controller
from shared.configuration.open_api_configuration import custom_open_api
from shared.mapping import mapper
from game.mapping import ModelToResource, ResourceToModel
from game.domain.models import Board, Piece
from game.resources import BoardResource, PieceResource
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


mapper.add_mapping(Piece, PieceResource, ModelToResource.piece_to_piece_resource)
mapper.add_mapping(PieceResource, Piece, ResourceToModel.piece_resource_to_piece)
mapper.add_mapping(Board, BoardResource, ModelToResource.board_to_board_resource)
mapper.add_mapping(BoardResource, Board, ResourceToModel.board_resource_to_board)

app.include_router(game_controller)
app.openapi = lambda: custom_open_api(app.routes)
