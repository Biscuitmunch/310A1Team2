from time import time
import pygame
import os
import time
import random
pygame.font.init()

WIDTH = 700
HEIGHT = 700
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invaders")

# Generate and sync images
# Background
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets","background-space.png")),(WIDTH,HEIGHT)) 

# Ships
RED_SHIP = pygame.image.load(os.path.join("assets","ship_red.png"))
GREEN_SHIP = pygame.image.load(os.path.join("assets","ship_green.png"))
BLUE_SHIP = pygame.image.load(os.path.join("assets","ship_blue.png"))
YELLOW_SHIP = pygame.image.load(os.path.join("assets","ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets","laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets","laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets","laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets","laser_yellow.png"))

def main():
    run = True
    
    # Set frame speed and clock- fits any device
    clock = pygame.time.Clock()
    FPS = 60

    level = 1
    lives = 5
    main_font = pygame.font.SysFont("monospace", 25)

    def rerender_window():
        WINDOW.blit(BACKGROUND,(0,0))
        
        # render and draw labels
        lives_label = main_font.render(F"LIVES: {lives}",1,(255,255,255))
        level_label = main_font.render(F"LEVEL: {level}",1,(255,255,255))

        WINDOW.blit(lives_label,(10,10))
        WINDOW.blit(level_label,(10, (lives_label.get_height() + 10)))

        pygame.display.update()


    while run:
        clock.tick(FPS)
        rerender_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            
main()