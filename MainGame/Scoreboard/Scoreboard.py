import pygame

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
font = pygame.font.Font('MainGame/Scoreboard/resources/Roboto_MediumItalic.ttf', 45)

def startScoreboard():
    run = True
    scores_displayed = False
    screen.fill((0, 0, 0))
    while run == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif scores_displayed == False:
                with open(SNAKE_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    text = font.render("Snake High Score: " + line, True, (WHITE))
                    screen.blit(text, [50, 35])

                with open(INVADER_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    text = font.render("Invader High Score: " + line, True, (WHITE))
                    screen.blit(text, [50, 135])

                with open(ASTEROIDS_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    text = font.render("Asteroids High Score: " + line, True, (WHITE))
                    screen.blit(text, [50, 235])

                with open(PONG_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    text = font.render("Asteroids High Score: " + line, True, (WHITE))
                    screen.blit(text, [50, 335])

                





            pygame.display.flip()
            clock.tick(60)

        