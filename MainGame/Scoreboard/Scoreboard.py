import sys

import pygame
import Buttons.InstrucButton as Button

#font
pygame.font.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
SNAKE_HIGHSCORE_FILE_PATH = 'MainGame/Snake/snakeScore.txt'
INVADER_HIGHSCORE_FILE_PATH = 'MainGame/Invader/invaderScore.txt'
ASTEROIDS_HIGHSCORE_FILE_PATH = 'MainGame/Asteroids/asteroidsScore.txt'
PONG_HIGHSCORE_FILE_PATH = 'MainGame/Pong/pongScore.txt'

# Set window title
pygame.display.set_caption('Snake')
background_color = (255, 255, 255)

def startScoreboard():
    run = True
    scores_displayed = False
    screen.fill((0, 0, 0))

    

    while run == True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        button_font = pygame.font.Font("MainGame/Fonts/PressStart2P.ttf", 35)
        title_font = pygame.font.Font("MainGame/Fonts/PressStart2P.ttf", 50)
        font = pygame.font.Font("MainGame/Fonts/PressStart2P.ttf", 25)

        QUIT_BUTTON = Button.Button(image=None, pos=(125, 650), text_input="MENU", font=button_font, base_color="White", hovering_color="Green")
        QUIT_BUTTON.changeColor(PLAY_MOUSE_POS)
        QUIT_BUTTON.update(screen)

        TITLE_TEXT = title_font.render("Scoreboard", True, "White")
        TITLE_RECT = TITLE_TEXT.get_rect(center=(300, 70))
        screen.blit(TITLE_TEXT, TITLE_RECT)

        for event in pygame.event.get():
            # Press x button to close app
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()

            elif QUIT_BUTTON.checkForInput(PLAY_MOUSE_POS) and event.type == pygame.MOUSEBUTTONDOWN:
                run = False

            elif scores_displayed == False:
                with open(SNAKE_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    text = font.render("Snake High Score: " + line, True, (WHITE))
                    screen.blit(text, [50, 140])

                with open(INVADER_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    text = font.render("Space Invaders High Score: " + line, True, (WHITE))
                    screen.blit(text, [50, 240])

                with open(ASTEROIDS_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    text = font.render("Asteroids High Score: " + line, True, (WHITE))
                    screen.blit(text, [50, 340])

                with open(PONG_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    text = font.render("Pong High Score: " + line, True, (WHITE))
                    screen.blit(text, [50, 440])

                scores_displayed = True

            pygame.display.update()
            pygame.display.flip()
            clock.tick(60)

        