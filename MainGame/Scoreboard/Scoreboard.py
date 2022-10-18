from ast import While
from cgitb import small
from re import L
import sys
import pygame
import Buttons.InstrucButton as Button
import Settings
import Avatar.avatar as avatar

WIDTH = Settings.WIDTH
HEIGHT = Settings.HEIGHT

#font
pygame.font.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

SNAKE_HIGHSCORE_FILE_PATH = 'MainGame/Snake/snakeScore.txt'
INVADER_HIGHSCORE_FILE_PATH = 'MainGame/Invader/invaderScore.txt'
ASTEROIDS_HIGHSCORE_FILE_PATH = 'MainGame/Asteroids/asteroidsScore.txt'
PONG_HIGHSCORE_FILE_PATH = 'MainGame/Pong/pongScore.txt'


# Set window title
pygame.display.set_caption('Scoreboard')
background_color = (255, 255, 255)
font = pygame.font.Font('MainGame/Scoreboard/resources/Roboto_MediumItalic.ttf', 45)
small_font = pygame.font.Font('MainGame/Scoreboard/resources/Roboto_MediumItalic.ttf', 25)

def startScoreboard():
    run = True
    scores_displayed = False
    screen.fill((0, 0, 0))

    while run == True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        button_font = pygame.font.Font("MainGame/Fonts/PressStart2P.ttf", 35)
        title_font = pygame.font.Font("MainGame/Fonts/PressStart2P.ttf", 50)
        font = pygame.font.Font("MainGame/Fonts/PressStart2P.ttf", 25)

        QUIT_BUTTON = Button.Button(image=None, pos=(100, 70), text_input="MENU", font=button_font, base_color="White", hovering_color="Green")
        QUIT_BUTTON.changeColor(PLAY_MOUSE_POS)
        QUIT_BUTTON.update(screen)

        TITLE_TEXT = title_font.render("Scoreboard", True, "White")
        TITLE_RECT = TITLE_TEXT.get_rect(center=(WIDTH/2, 70))
        screen.blit(TITLE_TEXT, TITLE_RECT)

        for event in pygame.event.get():
            # Press x button to close app
            if event.type == pygame.QUIT:
                avatar.clear_tickets()
                pygame.display.quit()
                sys.exit()

            elif QUIT_BUTTON.checkForInput(PLAY_MOUSE_POS) and event.type == pygame.MOUSEBUTTONDOWN:
                run = False

            elif scores_displayed == False:
                with open(SNAKE_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    text = font.render("Snake High Score: " + line, True, "white")
                    text1 = small_font.render("Score 35 or Higher to earn 50 tickets", True, "white")
                    screen.blit(text, [50, 135])
                    screen.blit(text1, [100, 170])

                with open(INVADER_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    text = font.render("Space Invaders High Score: " + line, True, "white")
                    text1 = small_font.render("Score 50 or Higher to earn 50 tickets", True, "white")
                    screen.blit(text, [50, 235])
                    screen.blit(text1, [100, 270])

                with open(ASTEROIDS_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    text = font.render("Asteroids High Score: " + line, True, "white")
                    text1 = small_font.render("Score 150,000 or Higher to earn 50 tickets", True, "white")
                    screen.blit(text, [50, 335])
                    screen.blit(text1, [100, 370])


                with open(PONG_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    text = font.render("Pong High Score: " + line, True, "white")
                    text1 = small_font.render("Score 8 or Higher to earn 50 tickets", True, "white")
                    screen.blit(text, [50, 435])
                    screen.blit(text1, [100, 470])

                scores_displayed = True

            pygame.display.update()

            pygame.display.flip()
            clock.tick(60)

        