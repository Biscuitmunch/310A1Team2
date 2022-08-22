import pygame
import random
import math

pygame.init()


player_ship = pygame.image.load('MainGame/Asteroids/resources/Playership.png')
Asteroids_Background = pygame.image.load(
    'MainGame/Asteroids/resources/asteroidsBackground.png')
asteroid_Small = pygame.image.load(
    'MainGame/Asteroids/resources/smallAsteroid.png')
asteroid_MediumSmall = pygame.image.load(
    'MainGame/Asteroids/resources/mediumSmallAsteroid.png')
asteroid_MediumLarge = pygame.image.load(
    'MainGame/Asteroids/resources/mediumLargeAsteroid.png')
asteroid_Medium = pygame.image.load(
    'MainGame/Asteroids/resources/mediumAsteroid.png')
asteroid_Large = pygame.image.load(
    'MainGame/Asteroids/resources/largeAsteroid.png')
WHITE = (255, 255, 255)
FPS = 60
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
#increase rotate angle size for sharper turns
rotate_angle_size = 5
initial_angle = 0
player_ship_speed = 8
player_reverse_speed = 2
bullet_speed = 15
bullet_width = 5
bullet_height = 5
#rate that determines frequency of asteroids, lower equals more frequent
asteroid_time_slice = 25
asteroid_speed = 0.5
lives = 3
score = 0
max_asteroid_size = 150
number_asteroids = 6

HIGHSCORE_FILE_PATH = 'MainGame/Asteroids/asteroidsScore.txt'
pygame.display.set_caption('Asteroids')

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.Font('MainGame/Snake/resources/BPdotsSquareBold.otf', 25)


def read_high_score():
    with open(HIGHSCORE_FILE_PATH, "r") as high_score_read:
        high_score = high_score_read.readline()
    high_score_read.close()
    return high_score


def set_high_score(score):

    if score > 149000:
            with open("MainGame/Avatar/ticketCount.txt", "r") as ticket_read:
                ticket_count = ticket_read.readline()
                with open("MainGame/Avatar/ticketCount.txt", "w") as ticket_write: 
                    ticket_write.write(str(ticket_count + 50))
                ticket_write.close()
            ticket_read.close()

    # Open high score file and change high score if current game beat it
    with open(HIGHSCORE_FILE_PATH, "r") as high_score_read:
        high_score = high_score_read.readline()
        if int(high_score) < score:
            high_score = score
            with open(HIGHSCORE_FILE_PATH, "w") as high_score_write:
                high_score_write.write(str(high_score))
            high_score_write.close()
    high_score_read.close()


class Player_ship(object):
    def __init__(self):
        self.image = player_ship
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        #initially position ship in middle of screen
        self.x = WINDOW_WIDTH//2
        self.y = WINDOW_HEIGHT//2
        self.angle = initial_angle
        self.update_angle()

    #call this after turning or moving to update position and angle
    def update_angle(self):
        self.rotated_surface = pygame.transform.rotate(self.image, self.angle)
        self.rotated_rectangle = self.rotated_surface.get_rect()
        self.rotated_rectangle.center = (self.x, self.y)
        #plus 90 because ship is looking up  (pointed towards positive y axis) and radians start from going counter4er clockwise from positive x axis
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        #tip is front of the ship
        self.tip = (self.x + self.cosine * self.width//2,
                    self.y - self.sine * self.height//2)

    def turning_left(self):
        self.angle += rotate_angle_size
        self.update_angle()

    def turning_right(self):
        self.angle -= rotate_angle_size
        self.update_angle()

        #move forward
    def forward(self):
        #x, y axis
        self.x += self.cosine * player_ship_speed
        self.y -= self.sine * player_ship_speed
        self.update_angle()

    def reverse(self):
        self.x -= self.cosine * player_reverse_speed
        self.y += self.sine * player_reverse_speed
        self.update_angle()

    def draw(self, window):
        #display with updated angle direction
        window.blit(self.rotated_surface, self.rotated_rectangle)

    #checks if player horizontal or verticle position is beyond window width or height
    def move_back_in_bounds(self):
        if self.x > WINDOW_WIDTH:
            self.x = 0
        elif self.x < 0:
            self.x = WINDOW_WIDTH
        elif self.y > WINDOW_HEIGHT:
            self.y = 0
        elif self.y < 0:
            self.y = WINDOW_HEIGHT


class Bullet(object):

    def __init__(self):
        #Bullet begins at tip of player spaceship
        self.position = Player_ship.tip
        self.x, self.y = self.position
        self.width = bullet_width
        self.height = bullet_height
        self.cos = Player_ship.cosine
        self.sin = Player_ship.sine
        #directional speed changes based on direction of playership
        self.x_velocity = self.cos * bullet_speed
        self.y_velocity = self.sin * bullet_speed

    def move(self):
        self.x += self.x_velocity
        self.y -= self.y_velocity

    def draw(self, win):
        pygame.draw.rect(win, WHITE, [self.x, self.y, self.width, self.height])

    def check_out_of_bounds(self):
        if self.x < -0 or self.x > WINDOW_WIDTH or self.y > WINDOW_HEIGHT or self.y < 0:
            return True


class Asteroid(object):
    def __init__(self, size):
        self.size = size
        #5 asteroids of different sizes
        if self.size == 1:
            self.image = asteroid_Small
        elif self.size == 2:
            self.image = asteroid_MediumSmall
        elif self.size == 3:
            self.image = asteroid_Medium
        elif self.size == 4:
            self.image = asteroid_MediumLarge
        else:
            self.image = asteroid_Large

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        #random position where Asteroid enters from. 150 being maximum image size, it always spawns at least 150 outside of screen
        self.random_entry_position = random.choice([(random.randrange(0, WINDOW_WIDTH-150), random.choice(
            [-max_asteroid_size, WINDOW_HEIGHT + max_asteroid_size])), (random.choice([-max_asteroid_size, WINDOW_WIDTH + max_asteroid_size]), random.randrange(0, WINDOW_HEIGHT - max_asteroid_size))])
        self.x, self.y = self.random_entry_position
        #where it spawns dictates which direction it heads. if its on the left side it goes right. if it spawns from above it goes down.
        if self.x < WINDOW_WIDTH//2:
            self.x_direction = 1
        else:
            self.x_direction = -1
        if self.y < WINDOW_HEIGHT//2:
            self.y_direction = 1
        else:
            self.y_direction = -1

        size_speed_factor = asteroid_speed*(number_asteroids-self.size)
        self.x_velocity = self.x_direction * \
            random.randrange(1, 4) * size_speed_factor
        self.y_velocity = self.y_direction * \
            random.randrange(1, 4) * size_speed_factor

    def check_out_of_bounds(self):
        #151 is used to be one more than where it would spawn, prevents buggy behaviour.
        if self.x < (-max_asteroid_size+1) or self.x > WINDOW_WIDTH + (max_asteroid_size + 1) or self.y > WINDOW_HEIGHT + (max_asteroid_size + 1) or self.y < -(max_asteroid_size + 1):
            return True

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


def draw_window():
    window.blit(Asteroids_Background, (0, 0))
    Player_ship.draw(window)

    game_over_text = font.render(
        'Press Space to Play again or Q to Quit to Menu', 1, WHITE)
    number_of_lives_text = font.render('Lives: ' + str(lives), 1, WHITE)
    score_text = font.render('Score: ' + str(score), 1, WHITE)
    new_high_score_text = font.render('New HighScore: ' + str(score), 1, WHITE)

    for b in bullets:
        b.draw(window)
    for a in asteroids:
        a.draw(window)

    if game_over:
        window.blit(game_over_text, (WINDOW_WIDTH//2-game_over_text.get_width() //
                    2, WINDOW_HEIGHT//2 - game_over_text.get_height()//2))

        high_score = read_high_score()
        if score > int(high_score):
            window.blit(new_high_score_text, (WINDOW_WIDTH//2-new_high_score_text.get_width() //
                                              2, WINDOW_HEIGHT//2 - new_high_score_text.get_height()//2 - 100))

    window.blit(score_text, (200, 25))
    window.blit(number_of_lives_text, (25, 25))
    pygame.display.update()


#creates two new asteroids one size lower than itself, this is called when a Asteroid is hit with a Bullet
def spawn_asteroids(size):
    new_asteroid1 = Asteroid(size-1)
    new_asteroid2 = Asteroid(size-1)
    new_asteroid1.x = asteroid.x
    new_asteroid2.x = asteroid.x
    new_asteroid1.y = asteroid.y
    new_asteroid2.y = asteroid.y
    asteroids.append(new_asteroid1)
    asteroids.append(new_asteroid2)


Player_ship = Player_ship()
bullets = []
asteroids = []

clock = pygame.time.Clock()

count = 0
game_over = False
running = True


def start_asteroids():
    global running 
    global count
    global game_over
    global lives
    global score
    global asteroid
    running = True
    


    while running:
        clock.tick(FPS)
        count += 1
        if not game_over:
            #randomly chosen new Asteroid will apear every time slice time past
            if count % asteroid_time_slice == 0:
                asteroidSize = random.choice(
                    [1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5])
                asteroids.append(Asteroid(asteroidSize))

            #makes player ship wrap around the screen
            Player_ship.move_back_in_bounds()

            for asteroid in asteroids:
                asteroid.x += asteroid.x_velocity
                asteroid.y += asteroid.y_velocity
                if asteroid.check_out_of_bounds():
                    asteroids.pop(asteroids.index(asteroid))
                    #check collision of Asteroid and player. same logic as below for bullets. figures out if player is inside Asteroid
                if (Player_ship.x >= asteroid.x and Player_ship.x <= asteroid.x + asteroid.width) or (Player_ship.x + Player_ship.width >= asteroid.x and Player_ship.x + Player_ship.width <= asteroid.x + asteroid.width):
                    if (Player_ship.y >= asteroid.y and Player_ship.y <= asteroid.y + asteroid.height) or (Player_ship.y + Player_ship.height >= asteroid.y and Player_ship.y + Player_ship.height <= asteroid.y + asteroid.height):
                        lives -= 1
                        asteroids.pop(asteroids.index(asteroid))
                        #break because if steroid is popped out of list but then checked in Bullet collision, it will cause errors
                        break

                for bullet in bullets:
                    #checking for Bullet collision with Asteroid: Bullet is both horizontally and vertically inside the Asteroid.
                    if (bullet.x + bullet.width >= asteroid.x and bullet.x + bullet.width <= asteroid.x + asteroid.width) or (bullet.x >= asteroid.x and bullet.x <= asteroid.x + asteroid.width):
                        if (bullet.y + bullet.height >= asteroid.y and bullet.y + bullet.height <= asteroid.y + asteroid.height) or (bullet.y >= asteroid.y and bullet.y <= asteroid.y + asteroid.height):
                            if asteroid.size > 1:
                                spawn_asteroids(asteroid.size)
                                #increase score, smaller size equals more score, number of asteroids = 6

                                score += (number_asteroids-asteroid.size)*500
                            #both Asteroid and Bullet disapear
                            asteroids.pop(asteroids.index(asteroid))
                            bullets.pop(bullets.index(bullet))

            if lives == 0:
                game_over = True

            for bullet in bullets:
                bullet.move()
                if bullet.check_out_of_bounds():
                    bullets.pop(bullets.index(bullet))

            #capture player input (WASD)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                Player_ship.turning_left()
            if keys[pygame.K_RIGHT]:
                Player_ship.turning_right()
            if keys[pygame.K_UP]:
                Player_ship.forward()
            if keys[pygame.K_DOWN]:
                Player_ship.reverse()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.set_caption("Arcade Menu")
                game_over = True
                #move to menu here
                running = False
                asteroids.clear()
                set_high_score(score)  # save highscore in text doc
                break #                                                                     ======
            # Q press quits to main menu
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                # if event.key == pygame.K_q:
                pygame.display.set_caption("Arcade Menu")
                game_over = True
                asteroids.clear()
                #go to main menu here

            #capture spacebar input. Done this way to prevent holding spacebar creating infinite bullets
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not game_over:
                    bullets.append(Bullet())
                else:
                    game_over = False
                    set_high_score(score)
                    lives = 3
                    score = 0
                    asteroids.clear()

        draw_window()


                                                                        
