from disco.level.parse import LevelObject, ParsedLine, parse_level


class Level:
    def __init__(self, objs: list[ParsedLine]):
        self.objs = objs

    @staticmethod
    def from_path(path: str) -> "Level":
        objs: list[ParsedLine] = []
        for obj in parse_level(path):
            if obj.ty == LevelObject.WALL:
                print(globals())
                raise NotImplementedError(
                    f"{__name__}.Level.from_path needs Platform at this point"
                )
        return objs
