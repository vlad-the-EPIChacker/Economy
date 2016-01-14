import pygame
import colors
import time
from pygame.locals import *
import sys
pygame.init()
(width, height) = (1300, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
myfont = pygame.font.SysFont("Menlo Regular", 50)
prompt='>'
while True:
    time.sleep(1/60.)
    screen.fill(colors.simple_color.black)
    label = myfont.render(prompt, 0, colors.simple_color.green)
    screen.blit(label, (0, 710))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shut=True
            pygame.quit()
        elif event.type == KEYDOWN:
            prompt=prompt+chr(event.key)