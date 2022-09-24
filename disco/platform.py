import pygame

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
