from ast import While
from cgitb import small
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

SNAKE_PLAYED_FILE_PATH = 'MainGame/Snake/snakePlayed.txt'
INVADERS_PLAYED_FILE_PATH = 'MainGame/Invader/invaderPlayed.txt'
ASTEROIDS_PLAYED_FILE_PATH = 'MainGame/Asteroids/asteroidsPlayed.txt'
PONG_PLAYED_FILE_PATH = 'MainGame/Pong/pongPlayed.txt'
BREAKOUT_PLAYED_FILE_PATH = 'MainGame/Breakout/breakoutPlayed.txt'

SPACE = "          "


# Set window title
pygame.display.set_caption('Snake')
background_color = (255, 255, 255)
font = pygame.font.Font('MainGame/Scoreboard/resources/Roboto_MediumItalic.ttf', 45)
small_font = pygame.font.Font('MainGame/Scoreboard/resources/Roboto_MediumItalic.ttf', 25)
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
                    text1 = small_font.render("Score 35 or Higher to earn 50 tickets", True, (WHITE))
                    screen.blit(text, [50, 135])
                    screen.blit(text1, [700, 145])


                with open(INVADER_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    text = font.render("Space Invaders High Score: " + line, True, (WHITE))
                    text1 = small_font.render("Score 50 or Higher to earn 50 tickets", True, (WHITE))
                    screen.blit(text, [50, 235])
                    screen.blit(text1, [700, 245])

                with open(ASTEROIDS_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    text = font.render("Asteroids High Score: " + line, True, (WHITE))
                    text1 = small_font.render("Score 150,000 or Higher to earn 50 tickets", True, (WHITE))
                    screen.blit(text, [50, 335])
                    screen.blit(text1, [700, 345])

                with open(PONG_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    text = font.render("Pong High Score: " + line, True, (WHITE))
                    text1 = small_font.render("Score 8 or Higher to earn 50 tickets", True, (WHITE))
                    screen.blit(text, [50, 435])
                    screen.blit(text1, [700, 445])

                with open(SNAKE_PLAYED_FILE_PATH) as file: 
                    snake_played = file.readline()
                
                with open(INVADERS_PLAYED_FILE_PATH) as file: 
                    invaders_played = file.readline()

                with open(ASTEROIDS_PLAYED_FILE_PATH) as file: 
                    asteroids_played = file.readline()

                with open(PONG_PLAYED_FILE_PATH) as file: 
                    pong_played = file.readline()

                with open(BREAKOUT_PLAYED_FILE_PATH) as file: 
                    breakout_played = file.readline()


                text = small_font.render("Times played", True, (WHITE))
                text1 = small_font.render("Snake: " + snake_played + SPACE + "Space Invaders: " + invaders_played + SPACE + "Asteroids: " + asteroids_played + SPACE + "Pong: " + pong_played + SPACE + "Breakout: " + breakout_played, True, (WHITE))
                screen.blit(text, [50, 590])
                screen.blit(text1, [50, 635])

                scores_displayed = True

            pygame.display.flip()
            clock.tick(60)

def increase_playcount(File_Path):
    with open(File_Path, "r") as play_count_read:
            times = int(play_count_read.readline())
            times += 1
            with open(File_Path, "w") as play_count_write: 
                play_count_write.write(str(times))
            play_count_write.close()
    play_count_write.close()

        