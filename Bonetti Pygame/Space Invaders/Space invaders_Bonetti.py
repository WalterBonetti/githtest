import pygame
from pygame.locals import *

clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")


bg = pygame.image.load("img/bg.png")

def draw_bg():
    screen.blit(bg, (0,0))


run = True
while run:

    clock.tick(fps)
    
    draw_bg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    
pygame.quit()
