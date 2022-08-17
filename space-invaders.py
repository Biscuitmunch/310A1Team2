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

# Abstract ship class that contains basic attributes of any space ship
class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None
        self.laser_image = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, area):
        area.blit(self.ship_image, (self.x, self.y))

    def get_width(self):
        return self.ship_image.get_width()

    def get_height(self):
        return self.ship_image.get_height()


# Player ship class that extends Ship
class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_image = YELLOW_SHIP
        self.laser_image = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.max_health = health

# Alien ship class that extends Ship
class Enemy(Ship):
    
    # Colour map for association of ship's colour to the image of its laser and itself
    COLOUR_DICT = {
        "red": (RED_SHIP, RED_LASER),
        "green": (GREEN_SHIP, GREEN_LASER),
        "blue": (BLUE_SHIP, BLUE_LASER)
    }


    def __init__(self, x, y, colour, health=100):
        super().__init__(x, y, health)
        self.ship_image, self.laser_image = self.COLOUR_DICT[colour]
        self.mask = pygame.mask.from_surface(self.ship_image)

    def move(self, speed):
        self.y += speed

def main():
    
    run = True
    main_font = pygame.font.SysFont("monospace", 25)
    
    # Set frame speed and clock- fits any device
    clock = pygame.time.Clock()
    FPS = 60

    # Speed = How many pixels moved per key press relative to clock speed
    player_speed = 5

    level = 0
    lives = 5
    
    # CREATE ENEMIES
    enemies = []
    wave_length = 5
    enemy_speed = 1


    # CREATE PLAYER
    player = Player(300, 600)

    def rerender_window():
        WINDOW.blit(BACKGROUND,(0,0))
        
        # render and draw labels
        lives_label = main_font.render(F"LIVES: {lives}",1,(255,255,255))
        level_label = main_font.render(F"LEVEL: {level}",1,(255,255,255))

        WINDOW.blit(lives_label,(10,10))
        WINDOW.blit(level_label,(10, (lives_label.get_height() + 10)))

        for enemy in enemies:
            enemy.draw(WINDOW)

        player.draw(WINDOW)

        pygame.display.update()


    while run:
        clock.tick(FPS)
        
        if len(enemies) == 0:
            level += 1
            wave_length += 5

            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red","blue","green"]))
                enemies.append(enemy)

        for event in pygame.event.get():

            # When the close button is clicked on window
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and (player.x + player_speed > 0): # moving left using left arrow key
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and (player.x + player_speed + player.get_width() < WIDTH): # moving right using right arrow key
            player.x += player_speed
        if keys[pygame.K_UP] and (player.y - player_speed > 0): # moving up using up arrow key
            player.y -= player_speed
        if keys[pygame.K_DOWN] and (player.y + player_speed + player.get_height() < HEIGHT): # moving down using down arrow key
            player.y += player_speed

        for enemy in enemies[:]:
            enemy.move(enemy_speed)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        rerender_window()
        
            
main()