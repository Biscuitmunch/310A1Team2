
import Settings
import sys
from time import time
import pygame
import os
import random
import Avatar.avatar as avatar
import Scoreboard.Scoreboard as scoreboard
pygame.font.init()

WIDTH = Settings.WIDTH
HEIGHT = Settings.HEIGHT
FPS = Settings.FPS

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
resources_path = "MainGame/Invader/resources"
break_loops = False
score = 0
HIGHSCORE_FILE_PATH = 'MainGame/Invader/invaderScore.txt'

# Generate and sync images
# Background
BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join(resources_path, "background-space.png")), (WIDTH, HEIGHT))

BACKGROUND1 = pygame.transform.scale(pygame.image.load(
    os.path.join(resources_path, "background-space-1.png")), (WIDTH, HEIGHT))

BACKGROUND2 = pygame.transform.scale(pygame.image.load(
    os.path.join(resources_path, "background-space-2.png")), (WIDTH, HEIGHT))

BACKGROUND3 = pygame.transform.scale(pygame.image.load(
    os.path.join(resources_path, "background-space-3.png")), (WIDTH, HEIGHT))

# Ships
RED_SHIP = pygame.image.load(os.path.join(resources_path, "ship_red.png"))
GREEN_SHIP = pygame.image.load(os.path.join(resources_path, "ship_green.png"))
BLUE_SHIP = pygame.image.load(os.path.join(resources_path, "ship_blue.png"))
YELLOW_SHIP = pygame.image.load(os.path.join(resources_path, "ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join(resources_path, "laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join(resources_path, "laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join(resources_path, "laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join(resources_path, "laser_yellow.png"))

# Laser class coded to make sure laser does not follow player when player moves in x direction


class Laser:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, area):
        area.blit(self.image, (self.x, self.y))

    def move(self, speed):
        self.y += speed

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, object):
        return collide(object, self)


# Abstract ship class that contains basic attributes of any space ship (common between enemy and player ships)
class Ship:
    COOL_DOWN = FPS/2

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None
        self.laser_image = None
        self.lasers = []
        self.cool_down_clock = 0

    def draw(self, area):
        area.blit(self.ship_image, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(area)

    def move_lasers(self, speed, object):
        # increment cooldown period everytime the lasers move (every frame)
        self.cooldown()

        for laser in self.lasers:
            laser.move(speed)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(object):
                object.health -= 10
                self.lasers.remove(laser)

    # prevents user from spamming the shoot button
    def cooldown(self):
        if self.cool_down_clock >= self.COOL_DOWN:
            self.cool_down_clock = 0
        elif self.cool_down_clock > 0:
            self.cool_down_clock += 1

    def get_width(self):
        return self.ship_image.get_width()

    def get_height(self):
        return self.ship_image.get_height()

    def shoot(self):
        if self.cool_down_clock == 0:
            # Render lasers from tip of space ship

            ship_width = self.get_width()

            if self.laser_count == 1:
                laser = Laser(self.x + ship_width / 2  , self.y, self.laser_image)
                self.lasers.append(laser)

            if self.laser_count == 2:
                laser = Laser(self.x, self.y, self.laser_image)
                self.lasers.append(laser)
                laser = Laser(self.x + ship_width, self.y, self.laser_image)
                self.lasers.append(laser)

            if self.laser_count == 3:
                laser = Laser(self.x + ship_width / 2, self.y, self.laser_image)
                self.lasers.append(laser)
                laser = Laser(self.x - ship_width / 2, self.y, self.laser_image)
                self.lasers.append(laser)
                laser = Laser(self.x + ship_width * 1.5, self.y, self.laser_image)
                self.lasers.append(laser)

            if self.laser_count == 4:
                laser = Laser(self.x + ship_width / 2, self.y + ship_width, self.laser_image)
                self.lasers.append(laser)
                laser = Laser(self.x - ship_width / 2, self.y + 10, self.laser_image)
                self.lasers.append(laser)
                laser = Laser(self.x + ship_width * 1.5, self.y + 10, self.laser_image)
                self.lasers.append(laser)
                laser = Laser(self.x + ship_width / 2, self.y, self.laser_image)
                self.lasers.append(laser)

            self.cool_down_clock = 1


# Player ship class that extends Ship
class Player(Ship):

    laser_count = 1

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_image = YELLOW_SHIP
        self.laser_image = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.max_health = health

    # Override parent's move_lasers method to suit player lasers hitting multiple enemies
    def move_lasers(self, speed, objects):
        global score
        # increment cooldown period everytime the lasers move (every frame)
        self.cooldown()

        for laser in self.lasers:
            laser.move(speed)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for object in objects:
                    if laser.collision(object):
                        objects.remove(object)
                        self.lasers.remove(laser)
                        score += 1

    def draw(self, area):
        super().draw(area)
        self.health_bar(area)

    def health_bar(self, area):
        # create max health green bar and overlay diminishing health with changing width red bar
        bar_height = 10
        ship_height = self.ship_image.get_height()
        ship_width = self.ship_image.get_width()


        # args:
        #   starting x cord
        #   starting y cord
        #   length of the bar in x cord
        #   height of the bar in y cord

        # Background Red Bar
        pygame.draw.rect(area, (255, 0, 0), (
            self.x, 
            self.y + ship_height + bar_height,
            ship_width,
            bar_height))

        # Foreground Green Bar (Health)
        health_fraction_calc = self.health/self.max_health
        pygame.draw.rect(area, (0, 255, 0), (
            self.x, 
            self.y + ship_height + bar_height, 
            ship_width * health_fraction_calc, 
            bar_height))


# Alien ship class that extends Ship
class Enemy(Ship):

    laser_count = 1

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


# check if masks of two objects overlap relative to their top left coordinates
def collide(object1, object2):
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y

    return object1.mask.overlap(object2.mask, (offset_x, offset_y)) != None


def main():

    global break_loops
    main_font = pygame.font.Font('MainGame/Fonts/BPdotsSquareBold.otf', 25)
    game_over_font = pygame.font.SysFont("monospace", 60)

    # Set frame speed and clock- fits any device
    clock = pygame.time.Clock()

    # Speed = How many pixels moved per key press relative to clock speed
    player_speed = 7
    laser_speed = 5
    enemy_speed = 1

    # probability that enemy shoots every second is 1/enemy_shooting_frequency
    enemy_shooting_freq = 100

    level = 0
    lives = 5
    game_over = False
    game_over_clock = 0
    break_loops = False

    # CREATE ENEMIES
    enemies = []
    wave_length = 10

    # CREATE PLAYER
    player = Player(300, 570)

    def rerender_window():

        if level != 0:
            if level % 4 == 1:
                WINDOW.blit(BACKGROUND, (0, 0))
            if level % 4 == 2:
                WINDOW.blit(BACKGROUND1, (0, 0))
            if level % 4 == 3:
                WINDOW.blit(BACKGROUND2, (0, 0))
            if level % 4 == 0:
                WINDOW.blit(BACKGROUND3, (0, 0))

        # Render labels
        lives_label = main_font.render(F"LIVES: {lives}", 1, (255, 255, 255))
        score_label = main_font.render(F"SCORE: {score}", 1, (255, 255, 255))
        level_label = main_font.render(F"LEVEL: {level}", 1, (255, 255, 255))
        enemies_label = main_font.render(F"ENEMIES: {len(enemies)} ", 1, ((255, 255, 255)))

        WINDOW.blit(lives_label, (10, 10))
        WINDOW.blit(score_label, (10, (lives_label.get_height() + 20)))
        WINDOW.blit(level_label, (10, ((lives_label.get_height() + 10)*2) + 10))
        WINDOW.blit(enemies_label, (10, ((lives_label.get_height() + 10)*3) + 10))

        if game_over:
            game_over_label = game_over_font.render(
                "GAME OVER", 1, (255, 255, 255))
            WINDOW.blit(game_over_label, (WIDTH/2 -
                        game_over_label.get_width()/2, HEIGHT/2))

        # Render enemies and player
        for enemy in enemies:
            enemy.draw(WINDOW)

        player.draw(WINDOW)

        pygame.display.update()

    while break_loops == False:
        global score
        clock.tick(FPS)
        rerender_window()

        # Scenario where player has lost display the game over text for 3 seconds
        if lives <= 0 or player.health <= 0:
            game_over = True
            set_high_score(score)
            score = 0
            game_over_clock += 1
            break

        if game_over:
            if game_over_clock > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1

            if level != 1:

                # Add random amount of enemy
                wave_length += random.choice([3, 5, 7])

                # Add enemy shooting change
                if enemy_shooting_freq > 30:
                    enemy_shooting_freq -= 5

                # Add enemy speed
                if enemy_speed < 3:
                    enemy_speed += 0.1

                # Regen player health
                player.health += 30
                # Check overflow
                if player.health > 100:
                    player.health = 100

                if level == 3:
                    player.laser_count = 2
                    player_speed += 1
                if level == 5:
                    player.laser_count = 3
                    player_speed += 1
                if level == 7:
                    player.laser_count = 4
                    player_speed += 1

            for i in range(wave_length):
                enemy = Enemy(random.randrange(
                    200, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            # Press x button to close app
            if event.type == pygame.QUIT:
                avatar.clear_tickets()
                pygame.display.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # moving left using left arrow key
        if keys[pygame.K_LEFT] and (player.x + player_speed > 0):
            player.x -= player_speed
        # moving right using right arrow key
        if keys[pygame.K_RIGHT] and (player.x + player_speed + player.get_width() < WIDTH):
            player.x += player_speed
        # moving up using up arrow key
        if keys[pygame.K_UP] and (player.y - player_speed > 0):
            player.y -= player_speed
        # moving down using down arrow key
        if keys[pygame.K_DOWN] and (player.y + player_speed + player.get_height() + 15 < HEIGHT):
            player.y += player_speed
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_speed)
            enemy.move_lasers(laser_speed, player)

            # Probability that enemy shoots
            if random.randrange(0, enemy_shooting_freq*FPS) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)

            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        # negative speed so lasers go up
        player.move_lasers(-laser_speed, enemies)

       
            
def set_high_score(score):
    if score > 49:
        avatar.add_tickets()

    # Open high score file and change high score if current game beat it
    with open(HIGHSCORE_FILE_PATH, "r") as high_score_read:
        high_score = high_score_read.readline()
        if int(high_score) < score:
            high_score = score
            with open(HIGHSCORE_FILE_PATH, "w") as high_score_write: 
                high_score_write.write(str(high_score))
            high_score_write.close()
    high_score_read.close()



def set_high_score(score):
    # Open high score file and change high score if current game beat it
    with open(HIGHSCORE_FILE_PATH, "r") as high_score_read:
        high_score = high_score_read.readline()
        if int(high_score) < score:
            high_score = score
            with open(HIGHSCORE_FILE_PATH, "w") as high_score_write:
                high_score_write.write(str(high_score))
            high_score_write.close()
    high_score_read.close()
