from game.resources.piece_resource import PieceResource
from pydantic import BaseModel


class BoardResource(BaseModel):
    player_pieces: list[PieceResource]
    ai_pieces: list[PieceResource]
