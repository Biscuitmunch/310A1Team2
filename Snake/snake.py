from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import random
from enum import Enum
from collections import namedtuple


pygame.init()
font = pygame.font.Font('Snake/BPdotsSquareBold.otf', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

BLOCKSIZE = 20
SPEED = 10

# Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
CHERRYSTALK = (94, 51, 35)
SNAKE = (98, 255, 0)
GRASS = (8, 36, 19)

class SnakeGame:

    def __init__(self, width = 1000, height = 480):
        # Set display resolution
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))

        # Set game caption
        pygame.display.set_caption('Snake')
        
        self.clock = pygame.time.Clock()

        # Set Starting direction
        self.direction = Direction.RIGHT

        # Set starting position of snake
        self.head = Point(self.width/2, self.height/2)
        self.snake = [self.head,
                      Point(self.head.x-BLOCKSIZE, self.head.y),
                      Point(self.head.x-(2*BLOCKSIZE), self.head.y)]

        # Set score and food defaults
        self.score = 0
        self.food = None

        # Place food on level
        self.placeFood()

    def placeFood(self):
        # Find a random x and y coordinate on the display
        x = random.randint(0, (self.width-BLOCKSIZE)//BLOCKSIZE)*BLOCKSIZE
        y = random.randint(0, (self.height-BLOCKSIZE)//BLOCKSIZE)*BLOCKSIZE

        # Place food omn the level
        self.food = Point(x, y)

        # If food is inside snake, try again
        if self.food in self.snake:
            self.placeFood()
        
    def playStep(self, lastDirection):
        # User Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Set direction to whichever arrow key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and lastDirection is not Direction.RIGHT:
                    self.direction = lastDirection = Direction.LEFT
                elif event.key == pygame.K_RIGHT and lastDirection is not Direction.LEFT:
                    self.direction = lastDirection = Direction.RIGHT
                elif event.key == pygame.K_UP and lastDirection is not Direction.DOWN:
                    self.direction = lastDirection = Direction.UP
                elif event.key == pygame.K_DOWN and lastDirection is not Direction.UP:
                    self.direction = lastDirection = Direction.DOWN
                    
        # Move
        self.move(self.direction)
        self.snake.insert(0, self.head)
        
        # Check if lost
        gameOver = False
        if self.isHurt():
            gameOver = True
            return gameOver, self.score, lastDirection
        
        # Take step action
        if self.head == self.food:
            self.score += 1
            self.placeFood()
            
        else:
            self.snake.pop()
        
        # Update UI and Clock
        self.updateUI()
        self.clock.tick(SPEED)
        
        # Game over and score
        return gameOver, self.score, lastDirection

        
    def updateUI(self):
        # Set background to grass colour
        self.display.fill(GRASS)

        for point in self.snake:
            
            #Draw snake segment
            pygame.draw.rect(self.display, SNAKE, pygame.Rect(point.x, point.y, BLOCKSIZE, BLOCKSIZE))
            pygame.draw.rect(self.display, RED, pygame.Rect(point.x, point.y, BLOCKSIZE/2, BLOCKSIZE/2))

        # Draw a cherry on the fruit position
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x+10, self.food.y+10, BLOCKSIZE/2, BLOCKSIZE/2))
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y+10, 6, 6))
        pygame.draw.rect(self.display, CHERRYSTALK, pygame.Rect(self.food.x+5, self.food.y, 5, 15))
        pygame.draw.rect(self.display, SNAKE, pygame.Rect(self.food.x+7, self.food.y, 8, 3))

        # Open high score file to display on screen
        with open('Snake/snakeScore.txt', "r") as highScoreRead:
            highScore = highScoreRead.readline()
        highScoreRead.close()

        # Display current score and high score on screen
        text = font.render("Score: " + str(self.score) + " High Score: " + highScore, True, WHITE)
        
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    def move(self, direction):
        # Get current snake head position
        x = self.head.x
        y = self.head.y

        # Move snake head in direction of arrow key pressed
        if direction == Direction.RIGHT:
            x += BLOCKSIZE
        elif direction == Direction.LEFT:
            x -= BLOCKSIZE
        elif direction == Direction.UP:
            y -= BLOCKSIZE
        elif direction == Direction.DOWN:
            y += BLOCKSIZE

        self.head = Point(x, y)

    def isHurt(self):
        # Check if snake head hit a wall
        if self.head.x > self.width - BLOCKSIZE or self.head.x < 0 or self.head.y > self.height - BLOCKSIZE or self.head.y < 0:
            return True

        # Check if snake head hit snake body
        if self.head in self.snake[1:]:
            return True

        return False
    
if __name__ == '__main__':
    game = SnakeGame()
    lastDirection = Direction.RIGHT
    while True:
        gameOver, score, lastDirection = game.playStep(lastDirection)
        if gameOver == True:
            break
    
    # Open high score file and change high score if current game beat it
    with open('Snake/snakeScore.txt', "r") as highScoreRead:
        highScore = highScoreRead.readline()
        if int(highScore) < score:
            highScore = score
            with open('Snake/snakeScore.txt', "w") as highScoreWrite: 
                highScoreWrite.write(str(highScore))
            highScoreWrite.close()
    highScoreRead.close()

    print('Final Score', score, 'High Score', highScore)
pygame.quit()