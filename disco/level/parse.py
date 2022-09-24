from enum import Enum, auto
from typing import Any, Generator


class LevelObject(Enum):
    "Enum of all the level objects."

    WALL = auto()
    "A wall, stationary."


class ParsedLine:
    "A parsed line from the level file. Contains the raw data."

    def __init__(self, ty: LevelObject, *props: Any):
        self.ty = ty
        self.props = props


def parse_level(path: str) -> Generator[ParsedLine, None, None]:
    with open(path) as f:
        for line in f.readlines():
            if line.startswith("#"):
                continue
            words = line.split(", ")
            rawty = words[0]
            if rawty == "wall":
                ty = LevelObject.WALL
            else:
                raise ValueError(f"Unknown level object type: {rawty}")
            props = words[1:]
            yield ParsedLine(ty, *props)
