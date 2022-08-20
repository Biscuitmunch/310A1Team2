import pygame
import random
import math

pygame.init()

BLACK = (0, 0, 0)
screen.fill(BLACK)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720




win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 

# font = pygame.font.Font('MainGame/Snake/resources/BPdotsSquareBold.otf', 25)
HIGHSCORE_FILE_PATH = 'MainGame/Asteroids/asteroidsScore.txt'

game_over = False


clock = pygame.time.Clock()

pygame.display.set_caption('Asteroids')


#under update UI from snake
        # # Display current score and high score on screen
        # text = font.render("Score: " + str(self.score) + " High Score: " + high_score, True, BLACK)
        # self.display.blit(text, [0, 0])
        # pygame.display.flip()

        #  def set_high_score(self, score):
        # # Open high score file and change high score if current game beat it
        # with open(HIGHSCORE_FILE_PATH, "r") as high_score_read:
        #     high_score = high_score_read.readline()
        #     if int(high_score) < score:
        #         high_score = score
        #         with open(HIGHSCORE_FILE_PATH, "w") as high_score_write: 
        #             high_score_write.write(str(high_score))
        #         high_score_write.close()
        # high_score_read.close()