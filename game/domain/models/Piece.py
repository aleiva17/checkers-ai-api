
class Piece:
    def __init__(self, is_queen: bool = None, x_coordinate: int = None, y_coordinate: int = None):
        self.__is_queen = is_queen
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate

    def set_is_queen(self, new_state: bool):
        self.__is_queen = new_state

    def set_coordinates(self, x_coordinate: int, y_coordinate: int):
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate

    def set_x_coordinate(self, x_coordinate: int):
        self.__x_coordinate = x_coordinate

    def set_y_coordinate(self, y_coordinate: int):
        self.__y_coordinate = y_coordinate

    def get_is_queen(self) -> bool:
        return self.__is_queen

    def get_coordinates(self) -> tuple[int, int]:
        return self.__x_coordinate, self.__y_coordinate

    def get_x_coordinate(self) -> int:
        return self.__x_coordinate

    def get_y_coordinate(self) -> int:
        return self.__y_coordinate
