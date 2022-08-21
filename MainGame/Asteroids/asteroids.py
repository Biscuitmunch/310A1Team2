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
white = (255, 255, 255)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
#increase rotate angle size for sharper turns
rotateAngleSize = 5
initialAngle = 0
playerShipSpeed = 8
playerReverseSpeed = 2
bulletSpeed = 15
bulletWidth = 5
bulletHeight = 5
#rate that determines frequency of asteroids, lower equals more frequent
asteroidTimeSlice = 25
asteroidSpeed = 0.5
lives = 3
score = 0


HIGHSCORE_FILE_PATH = 'MainGame/Asteroids/asteroidsScore.txt'
pygame.display.set_caption('Asteroids')

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
font = pygame.font.Font('MainGame/Snake/resources/BPdotsSquareBold.otf', 25)


def read_high_score():
    with open(HIGHSCORE_FILE_PATH, "r") as high_score_read:
        highScore = high_score_read.readline()
    high_score_read.close()
    return highScore

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
        
    #call this after turning or moving to update position and angle
    def updateAngle(self):
        self.rotatedSurface = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRectangle = self.rotatedSurface.get_rect()
        self.rotatedRectangle.center = (self.x, self.y)
        #plus 90 because ship is looking up  (pointed towards positive y axis) and radians start from going counter4er clockwise from positive x axis
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

        #move forward
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
    
    #checks if player horizontal or verticle position is beyond window width or height
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
        #random position where asteroid enters from. 150 being maximum image size, it always spawns at least 150 outside of screen
        self.randomEntryPosition = random.choice([(random.randrange(0, WINDOW_WIDTH-150), random.choice([-150, WINDOW_HEIGHT + 150])), (random.choice([-150, WINDOW_WIDTH + 150]), random.randrange(0, WINDOW_HEIGHT - 150))])
        self.x, self.y = self.randomEntryPosition
        #where it spawns dictates which direction it heads. if its on the left side it goes right. if it spawns from above it goes down.
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

    def checkOutOfBounds(self):
        #151 is used to be one more than where it would spawn, prevents buggy behaviour. 
        if self.x < -151 or self.x > WINDOW_WIDTH + 151 or self.y > WINDOW_HEIGHT +151 or self.y < -151:
            return True

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))





def drawWindow():
    window.blit(Asteroids_Background, (0,0))
    playerShip.draw(window)

    
    gameOverText = font.render('Press Space to Play again or Q to Quit to Menu', 1, white)
    numberOfLivesText = font.render('Lives: ' + str(lives), 1, white)
    scoreText = font.render('Score: ' + str(score), 1, white)
    newHighScoreText = font.render('New HighScore: ' + str(score), 1, white)

    for b in bullets:
        b.draw(window)
    for a in asteroids:
        a.draw(window)

    if game_over:
            window.blit(gameOverText, (WINDOW_WIDTH//2-gameOverText.get_width()//2, WINDOW_HEIGHT//2 - gameOverText.get_height()//2))
            
            highScore = read_high_score()
            if score > int(highScore):
                window.blit(newHighScoreText, (WINDOW_WIDTH//2-newHighScoreText.get_width()//2, WINDOW_HEIGHT//2 - newHighScoreText.get_height()//2 -100))



    window.blit(scoreText, (200, 25))
    window.blit(numberOfLivesText, (25, 25))
    pygame.display.update()



#creates two new asteroids one size lower than itself, this is called when a asteroid is hit with a bullet
def spawnAsteroids(size):
    newAsteroid1 = asteroid(size-1)
    newAsteroid2 = asteroid(size-1)
    newAsteroid1.x = a.x
    newAsteroid2.x = a.x
    newAsteroid1.y = a.y
    newAsteroid2.y = a.y
    asteroids.append(newAsteroid1)
    asteroids.append(newAsteroid2)


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
        #randomly chosen new asteroid will apear every time slice time past
        if count % asteroidTimeSlice == 0:
            asteroidSize = random.choice([1,1,1,1,2,2,3,4,4,5,5,5,5])
            asteroids.append(asteroid(asteroidSize))

        #makes player ship wrap around the screen
        playerShip.moveBackInBounds()

        for a in asteroids:
            a.x += a.xVelocity
            a.y += a.yVelocity
            if a.checkOutOfBounds():
                asteroids.pop(asteroids.index(a))
                #check collision of asteroid and player. same logic as below for bullets. figures out if player is inside asteroid
            if (playerShip.x >= a.x and playerShip.x <= a.x + a.width) or (playerShip.x + playerShip.width >= a.x and playerShip.x + playerShip.width <= a.x + a.width):
                if (playerShip.y >= a.y and playerShip.y <= a.y + a.height) or (playerShip.y + playerShip.height >= a.y and playerShip.y  + playerShip.height <= a.y + a.height):
                    lives -= 1
                    asteroids.pop(asteroids.index(a))
                    #break because if steroid is popped out of list but then checked in bullet collision, it will cause errors
                    break

            for b in bullets:
                #checking for bullet collision with asteroid: bullet is both horizontally and vertically inside the asteroid. 
                if (b.x + b.width >= a.x and b.x + b.width <= a.x + a.width) or (b.x >= a.x and b.x <= a.x + a.width):
                    if (b.y + b.height >= a.y and b.y + b.height <= a.y + a.height) or (b.y >= a.y and b.y <= a.y + a.height):
                        if a.size > 1:
                            spawnAsteroids(a.size)
                            #increase score, smaller size equals more score
                            score += (6-a.size)*500
                        #both asteroid and bullet disapear
                        asteroids.pop(asteroids.index(a))
                        bullets.pop(bullets.index(b))

        if lives == 0:
            game_over = True

        
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
            #move to menu here
            running = False
            set_high_score(score) #save highscore in text doc
           

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q: #Q press quits to main menu
                pygame.display.set_caption("Arcade Menu")
                #go to main menu here

        #capture spacebar input. Done this way to prevent holding spacebar creating infinite bullets
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_over:
                    bullets.append(bullet())
                else: 
                    game_over = False
                    set_high_score(score)
                    lives = 3
                    score = 0
                    asteroids.clear()
                    

    drawWindow()

            
pygame.quit()




