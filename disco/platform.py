from math import cos, sin
import pygame

import numpy as np
from disco.collidable import Collidable
from disco.renderable import Renderable


class Platform(Collidable, Renderable):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        theta: float,
        sprite: pygame.sprite.Sprite,
    ):
        super().__init__()
        self._transform = np.array(
            [[cos(theta), sin(theta), x], [-sin(theta), cos(theta), y], [0, 0, 1]]
        )

    def collides(self, other: Collidable) -> bool:
        return False

    @property
    def transform(self) -> np.array:
        return self._transform
