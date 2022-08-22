import pygame

#font
pygame.font.init()

screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()

HIGHSCORE_FILE_PATH = 'MainGame/Snake/snakeScore.txt'

# Set window title
pygame.display.set_caption('Snake')
background_color = (255, 255, 255)

highscore_surface = pygame.Surface((300, 400))
highscore_surface.fill((90, 100, 120))

myfont = pygame.font.SysFont('Comic Sans MS', 30)
highscores_visible = True


running = True
while running:
    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            with open(HIGHSCORE_FILE_PATH, "r") as file:
                line = file.readline()  # scores are one line
                high_scores = [int(s) for s in line.split()]  # read scores as integers

            for i, (score) in enumerate(high_scores):
                text = myfont.render('{}'.format(score), True, (0, 0, 0))
                highscore_surface.blit(text, (50, 30*i+5))

    
    if highscores_visible:
        screen.blit(highscore_surface, (50, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()