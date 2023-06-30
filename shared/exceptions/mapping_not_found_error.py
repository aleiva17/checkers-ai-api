
class MappingNotFoundError(Exception):
    def __init__(self, mapping: tuple):
        self.mapping = mapping

    def __str__(self):
        return f"Mapping from '{self.mapping[0]}' to '{self.mapping[1]}' not found."
