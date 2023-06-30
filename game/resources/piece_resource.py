from pydantic import BaseModel


class PieceResource(BaseModel):
    is_queen: bool
    x_coordinate: int
    y_coordinate: int
