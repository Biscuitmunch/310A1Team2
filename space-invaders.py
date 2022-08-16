from time import time
import pygame
import os
import time
import random

WIDTH = 700
HEIGHT = 700
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invaders")

# Generate and sync images
# Background
BACKGROUND = pygame.image.load(os.path.join("assets","background-space.png"))

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

