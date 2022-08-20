import pygame
import random
import math

pygame.init()



player_ship = pygame.image.load('MainGame/Asteroids/resources/playerShip.png')
Asteroids_Background = pygame.image.load('MainGame/Asteroids/resources/asteroidsBackground.png')
asteroid_Small = pygame.image.load('MainGame/Asteroids/resources/smallAsteroid.png')
asteroid_MediumSmall = pygame.image.load('MainGame/Asteroids/resources/mediumSmallAsteroid.png')
asteroid_MediumLarge = pygame.image.load('MainGame/Asteroids/resources/mediumLargeAsteroid.png')
asteroid_Medium = pygame.image.load('MainGame/Asteroids/resources/mediumAsteroid.png')

asteroid_Large = pygame.image.load('MainGame/Asteroids/resources/largeAsteroid.png')

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
rotateAngleSize = 5
initialAngle = 0
playerShipSpeed = 8
playerReverseSpeed=2
bulletSpeed = 15
bulletWidth = 5
bulletHeight = 5

#rate that determines frequency of asteroids, lower equals more frequent
asteroidTimeSlice = 25
asteroidSpeed = 0.5

white = (255, 255, 255)

pygame.display.set_caption('Asteroids')


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
# font = pygame.font.Font('MainGame/Snake/resources/BPdotsSquareBold.otf', 25)
HIGHSCORE_FILE_PATH = 'MainGame/Asteroids/asteroidsScore.txt'

class playerShip(object):
    def __init__(self):
        self.image = player_ship
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        #initially position ship in middle of screen
        self.x = WINDOW_WIDTH//2
        self.y = WINDOW_HEIGHT//2
        self.angle = initialAngle
        self.updateAngle()
        
    #call this after turning to update position and angle
    def updateAngle(self):
        self.rotatedSurface = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRectangle = self.rotatedSurface.get_rect()
        self.rotatedRectangle.center = (self.x, self.y)
        #plus 90 because ship is looking up  (pointed towards positive y axis) and radians start from going coutner clockwise from positive x axis
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        #tip is front of the ship
        self.tip = (self.x + self.cosine * self.width//2, self.y - self.sine * self.height//2)

    def turningLeft(self):
        self.angle += rotateAngleSize
        self.updateAngle()


    def turningRight(self):
        self.angle -= rotateAngleSize
        self.updateAngle()


    def Forward(self):
        #x, y axis
        self.x += self.cosine * playerShipSpeed
        self.y -= self.sine * playerShipSpeed
        self.updateAngle()

    def Reverse(self):
        self.x -= self.cosine *  playerReverseSpeed
        self.y += self.sine * playerReverseSpeed
        self.updateAngle()
    

    def draw(self, window):
        #display with updated angle direction
        window.blit(self.rotatedSurface, self.rotatedRectangle)
    
    #checks if player horizontal or verticle position is beyound window width or heigh
    def moveBackInBounds(self):
        if self.x > WINDOW_WIDTH:
            self.x = 0
        elif self.x < 0:
            self.x = WINDOW_WIDTH
        elif self.y > WINDOW_HEIGHT:
            self.y = 0
        elif self.y < 0:
            self.y = WINDOW_HEIGHT
        
        
        


class bullet(object):

    def __init__(self):
        #bullet begins at tip of player spaceship
        self.position = playerShip.tip
        self.x, self.y = self.position
        self.width = bulletWidth
        self.height = bulletHeight
        self.cos = playerShip.cosine 
        self.sin = playerShip.sine
        #directional speed changes based on direction of playership
        self.xVelocity = self.cos * bulletSpeed
        self.yVelocity = self.sin * bulletSpeed

    def move(self):
        self.x += self.xVelocity
        self.y -= self.yVelocity

    def draw(self, win):
        pygame.draw.rect(win, white, [self.x, self.y, self.width, self.height])

 
    def checkOutOfBounds(self):
        if self.x < -0 or self.x > WINDOW_WIDTH or self.y > WINDOW_HEIGHT or self.y < 0:
            return True

class asteroid(object):
    def __init__(self, size):
        self.size = size
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
        #random position where asteroid enters from
        self.randomEntryPosition = random.choice([(random.randrange(0, WINDOW_WIDTH-150), random.choice([-150, WINDOW_HEIGHT + 150])), (random.choice([-150, WINDOW_WIDTH + 150]), random.randrange(0, WINDOW_HEIGHT - 150))])
        self.x, self.y = self.randomEntryPosition
        if self.x < WINDOW_WIDTH//2:
            self.xDirection = 1
        else:
            self.xDirection = -1
        if self.y < WINDOW_HEIGHT//2:
            self.yDirection = 1
        else:
            self.yDirection = -1

        sizeSpeedFactor=asteroidSpeed*(6-self.size)
        self.xVelocity = self.xDirection * random.randrange(1,4) * sizeSpeedFactor
        self.yVelocity = self.yDirection * random.randrange(1,4)* sizeSpeedFactor


    def draw(self, win):
        win.blit(self.image, (self.x, self.y))





def drawWindow():
    window.blit(Asteroids_Background, (0,0))
    playerShip.draw(window)

    for b in bullets:
        b.draw(window)
    for a in asteroids:
        a.draw(window)
    
    pygame.display.update()



playerShip = playerShip()
bullets = []
asteroids = []

clock = pygame.time.Clock()

count=0
game_over = False
running = True
while running: 
    clock.tick(60)
    count +=1
    if not game_over:
        if count % asteroidTimeSlice == 0:
            asteroidSize = random.choice([1,1,1,1,2,2,3,4,4,5,5,5,5])
            asteroids.append(asteroid(asteroidSize))


        playerShip.moveBackInBounds()

        for a in asteroids:
            a.x += a.xVelocity
            a.y += a.yVelocity

        for b in bullets:
            b.move()
            if b.checkOutOfBounds():
                bullets.pop(bullets.index(b))

        #capture player input (WASD) 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            playerShip.turningLeft()
        if keys[pygame.K_d]:
            playerShip.turningRight()
        if keys[pygame.K_w]:
            playerShip.Forward()
        if keys[pygame.K_s]:
            playerShip.Reverse()

        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.display.set_caption("Arcade Menu")
                        running = False
                        #add set_high_score later

                    #capture spacebar input. Done this way to prevent holding spacebar creating infinite bullets 
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if not game_over:
                                bullets.append(bullet())

    drawWindow()

            


pygame.quit()


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


#under update UI from snake
        # # Display current score and high score on screen
        # text = font.render("Score: " + str(self.score) + " High Score: " + high_score, True, BLACK)
        # self.display.blit(text, [0, 0])
        # pygame.display.flip()

