from shared.domain.models import singleton
from shared.exceptions import MappingNotFoundError
from typing import Callable


@singleton
class Mapper:
    def __init__(self):
        self.__mapping = dict()

    def add_mapping(self, origin: type, destination: type, function: Callable):
        self.__mapping[(origin.__name__, destination.__name__)] = function

    def map(self, origin: object, destination: type):
        conversion_key = (origin.__class__.__name__, destination.__name__)

        if conversion_key not in self.__mapping:
            raise MappingNotFoundError(conversion_key)

        return self.__mapping[conversion_key](origin)
