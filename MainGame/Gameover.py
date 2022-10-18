import pygame
import sys
import Snake.snake as snake
import Buttons.InstrucButton as Button
import Pong.pong as pong
import Invader.space_invaders as invader
import Asteroids.asteroids as asteroids 
import Breakout.breakout as breakout
import Instructions


WIDTH = 1280
HEIGHT = 720

SNAKE_HIGHSCORE_FILE_PATH = 'MainGame/Snake/snakeScore.txt'
INVADER_HIGHSCORE_FILE_PATH = 'MainGame/Invader/invaderScore.txt'
ASTEROIDS_HIGHSCORE_FILE_PATH = 'MainGame/Asteroids/asteroidsScore.txt'
PONG_HIGHSCORE_FILE_PATH = 'MainGame/Pong/pongScore.txt'

class ScreenItem():
    def __init__(self, x, y, image):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))

    # Show the item
    def update(self):
        window = pygame.display.set_mode((WIDTH, HEIGHT))
        window.blit(self.image, self.rect)

    # Determine if mouse is interacting with item to perform further logic
    def mouse_over_button(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True


class gameover:

    def gameOver(self, game):
        running = True
        while running:            
            window = pygame.display.set_mode((WIDTH, HEIGHT))
            window.fill("black")
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            score_font = pygame.font.Font("MainGame/Buttons/PressStart2P.ttf", 35)
            title_font = pygame.font.Font("MainGame/Buttons/PressStart2P.ttf", 70)
            button_font = pygame.font.Font("MainGame/Buttons/PressStart2P.ttf", 35)

            OVER_TEXT = title_font.render("GAME OVER", True, "Red")

            # Set text and score for each game
            if game == "snake":
                with open(SNAKE_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  # scores are one line
                    HIGHSCORE_TEXT = score_font.render("HIGHSCORE: " + line, True, "Yellow")
            elif game == "pong":
                with open(PONG_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline()  
                    HIGHSCORE_TEXT = score_font.render("HIGHSCORE: " + line, True, "Yellow")
            elif game == "asteroids":
                with open(ASTEROIDS_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline() 
                    HIGHSCORE_TEXT = score_font.render("HIGHSCORE: " + line, True, "Yellow")
            elif game == "breakout":
                HIGHSCORE_TEXT = score_font.render("well done!", True, "Yellow") # breakout has no high score   
            elif game == "invader":
                with open(INVADER_HIGHSCORE_FILE_PATH, "r") as file:
                    line = file.readline() 
                    HIGHSCORE_TEXT = score_font.render("HIGHSCORE: " + line, True, "Yellow")

            # Show text
            OVER_RECT = OVER_TEXT.get_rect(center=(640, 300))
            window.blit(OVER_TEXT, OVER_RECT)
            
            HIGHSCORE_RECT = HIGHSCORE_TEXT.get_rect(center=(640, 400))
            window.blit(HIGHSCORE_TEXT, HIGHSCORE_RECT)

            # Navigation buttons
            PLAY_BUTTON = Button.Button(image=None, pos=(860, 550), text_input="PLAY AGAIN", font=button_font, base_color="White", hovering_color="Green")
            PLAY_BUTTON.changeColor(PLAY_MOUSE_POS)
            PLAY_BUTTON.update(window)
            QUIT_BUTTON = Button.Button(image=None, pos=(380, 550), text_input="MENU", font=button_font, base_color="White", hovering_color="Green")
            QUIT_BUTTON.changeColor(PLAY_MOUSE_POS)
            QUIT_BUTTON.update(window)

            # Check for clicks
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # x button exits the game window
                    pygame.display.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        # Go to requested game
                        if game == "snake":
                            snake_obj = snake.snake_game()
                            snake_obj.start_game()
                        elif game == "pong":
                            pong_obj = pong.PongGame()
                            pong_obj.start_game()
                        elif game == "asteroids":
                            running = False
                            asteroids.start_asteroids()
                        elif game == "breakout":
                            breakout.start_breakout()
                        elif game == "invader":
                            invader.main()
                        running = False
                            
                        
                    elif QUIT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        running = False

            pygame.display.update()
