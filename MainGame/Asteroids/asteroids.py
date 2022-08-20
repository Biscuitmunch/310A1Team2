import pygame
import random
import math

pygame.init()



player_ship = pygame.image.load('MainGame/Asteroids/resources/playerShip.png')
Asteroids_Background = pygame.image.load('MainGame/Asteroids/resources/AsteroidsBackground.png')

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
rotateAngleSize = 5
initialAngle = 0
playerShipSpeed = 7

pygame.display.set_caption('Asteroids')


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
# font = pygame.font.Font('MainGame/Snake/resources/BPdotsSquareBold.otf', 25)
HIGHSCORE_FILE_PATH = 'MainGame/Asteroids/asteroidsScore.txt'

class playerShip(object):
    def __init__(self):
        self.img = player_ship
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        #position ship in middle of screen
        self.x = WINDOW_WIDTH//2
        self.y = WINDOW_HEIGHT//2
        self.angle = initialAngle

        self.updateAngle()
        
    #call this after turning to update position and angle
    def updateAngle(self):
        self.rotatedSurface = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRectangle = self.rotatedSurface.get_rect()
        self.rotatedRectangle.center = (self.x, self.y)
        #plus 90 because ship is looking up  (pointed towards positive y axis) and radians start from going up from positive x axis
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
        self.x += self.cosine * playerShipSpeed
        self.y -= self.sine * playerShipSpeed
        self.updateAngle()

    def draw(self, window):
        #display with updated angle direction
        window.blit(self.rotatedSurface, self.rotatedRectangle)
        
        



def drawWindow():
    window.blit(Asteroids_Background, (0,0))

    playerShip.draw(window)
    pygame.display.update()



playerShip = playerShip()
clock = pygame.time.Clock()
game_over = False

while not game_over:
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.set_caption("Arcade Menu")
            game_over = True
            #add set_high_score later


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        playerShip.turningLeft()
    if keys[pygame.K_d]:
        playerShip.turningRight()
    if keys[pygame.K_w]:
        playerShip.Forward()
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

