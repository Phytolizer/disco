from disco.level.parse import LevelObject, ParsedLine, parse_level
from disco.platform import Platform
import pymunk


class Level:
    def __init__(self, objs: list[ParsedLine]):
        self.objs = objs
        self.space = pymunk.Space()  # Create a space relevant to the camera
        self.space.gravity = 0, -981  # set gravity for the space

    @staticmethod
    def from_path(path: str) -> "Level":
        objs: list[ParsedLine] = []
        for obj in parse_level(path):
            if obj.ty == LevelObject.WALL:
                topleft, bottomright = obj.props
                x1, y1 = map(float, topleft.split(" "))
                x2, y2 = map(float, bottomright.split(" "))
                objs.append(Platform(x1, y1, x2 - x1, y2 - y1, 0, None))
        return Level(objs)
