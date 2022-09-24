import pygame
import pymunk
from disco.platform import Platform

pygame.init()

window: pygame.Surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("disco")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 0, 0))
    pygame.display.update()
