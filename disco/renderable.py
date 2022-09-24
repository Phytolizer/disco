import pygame

from disco.transformable import Transformable


class Renderable(Transformable):
    def __init__(self, sprite: pygame.sprite.Sprite):
        self.sprite = sprite
