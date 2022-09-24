import numpy as np
import pygame
from pygame.draw import polygon

from disco.collidable import Collidable
from disco.renderable import Renderable
from disco.transformable import Transformable


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
        self._transform = Transformable.gen_transform(x, y, theta)

    def collides(self, other: Collidable) -> bool:
        return False

    @property
    def transform(self) -> np.array:
        return self._transform

    def render(self, surface: pygame.Surface, color: pygame.Color):
        polygon(
            surface,
            color,
            (
                (0, 0),
                (0, 1),
                (1, 1),
                (1, 0),
            ),
        )
