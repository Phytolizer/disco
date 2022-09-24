import pygame

import disco.player
from disco.level import Level

pygame.init()

window: pygame.Surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("disco")

lev = Level.from_path("levels/01.disco-level")

player = disco.player.Player(lev.space)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 0, 0))
    pygame.display.update()
