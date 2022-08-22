import pygame

#font
pygame.font.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

HIGHSCORE_FILE_PATH = 'MainGame/Snake/snakeScore.txt'

# Set window title
pygame.display.set_caption('Snake')
background_color = (255, 255, 255)


myfont = pygame.font.SysFont('Comic Sans MS', 30)

def startScoreboard():
    running = True
    screen.fill((90, 100, 120))
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                with open(HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    high_scores = [int(s) for s in line.split()]  # read scores as integers

                    text = myfont.render('{}'.format(high_scores), True, (0, 0, 0))
                    screen.blit(text, (50, 35))

        pygame.display.flip()
        clock.tick(60)
