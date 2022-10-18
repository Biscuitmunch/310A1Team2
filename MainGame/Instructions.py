import sys
import pygame
import Snake.snake as snake
import Buttons.InstrucButton as Button
import Pong.pong as pong
import Invader.space_invaders as invader
import Asteroids.asteroids as asteroids 
import Breakout.breakout as breakout
import Settings
import Avatar.avatar as avatar

WIDTH = Settings.WIDTH
HEIGHT = Settings.HEIGHT

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


class instructions:

    def play(self, game):
        running = True
        while running:            
            window = pygame.display.set_mode((WIDTH, HEIGHT))
            window.fill("black")
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            font = pygame.font.Font("MainGame/Fonts/PressStart2P.ttf", 25)
            title_font = pygame.font.Font("MainGame/Fonts/PressStart2P.ttf", 50)
            button_font = pygame.font.Font("MainGame/Fonts/PressStart2P.ttf", 35)

            # Game title

            #Set text for each game
            if game == "snake":
                PLAY_TEXT = title_font.render("SNAKE", True, "White")
                INSTRUC_TEXT_1 = font.render("use arrow keys to change directions", True, "White")
                INSTRUC_TEXT_2 = font.render("don’t run into any walls or your own tail", True, "White")
                INSTRUC_TEXT_3 = font.render("eat cherries to grow", True, "White")
            elif game == "pong":
                PLAY_TEXT = title_font.render("PONG", True, "White")
                INSTRUC_TEXT_1 = font.render("use arrow keys to move", True, "White")
                INSTRUC_TEXT_2 = font.render("don’t let the ball hit the wall", True, "White")
                INSTRUC_TEXT_3 = font.render("don't let the enemy score 5 points", True, "White")
            elif game == "asteroids":
                PLAY_TEXT = title_font.render("ASTEROIDS", True, "White")
                INSTRUC_TEXT_1 = font.render("use arrow keys to move", True, "White")
                INSTRUC_TEXT_2 = font.render("use spacebar to shoot", True, "White")
                INSTRUC_TEXT_3 = font.render("destroy asteroids to score points", True, "White")
            elif game == "breakout":
                PLAY_TEXT = title_font.render("BREAKOUT", True, "White")
                INSTRUC_TEXT_1 = font.render("use arrow keys to move", True, "White")
                INSTRUC_TEXT_2 = font.render("destroy all bricks to win", True, "White")
                INSTRUC_TEXT_3 = font.render("", True, "White")
                INSTRUC_IMG = pygame.transform.scale(pygame.image.load(
                    "MainGame/Buttons/breakoutInstruc.png").convert_alpha(), (1000,200))
                instruc_img = ScreenItem(640, 375, INSTRUC_IMG)
                instruc_img.update()
            elif game == "invader":
                PLAY_TEXT = title_font.render("INVADERS", True, "White")
                INSTRUC_TEXT_1 = font.render("use arrow keys to move", True, "White")
                INSTRUC_TEXT_2 = font.render("use spacebar to shoot", True, "White")
                INSTRUC_TEXT_3 = font.render("destroy all enemies to win", True, "White")

            #Show text
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
            window.blit(PLAY_TEXT, PLAY_RECT)
            
            INSTRUC_RECT_1 = INSTRUC_TEXT_1.get_rect(center=(640, 200))
            window.blit(INSTRUC_TEXT_1, INSTRUC_RECT_1)
            
            INSTRUC_RECT_2 = INSTRUC_TEXT_2.get_rect(center=(640, 250))
            window.blit(INSTRUC_TEXT_2, INSTRUC_RECT_2)
            
            INSTRUC_RECT_3 = INSTRUC_TEXT_3.get_rect(center=(640, 300))
            window.blit(INSTRUC_TEXT_3, INSTRUC_RECT_3)

            # Navigation buttons
            PLAY_BUTTON = Button.Button(image=None, pos=(900, 550), text_input="PLAY", font=button_font, base_color="White", hovering_color="Green")
            PLAY_BUTTON.changeColor(PLAY_MOUSE_POS)
            PLAY_BUTTON.update(window)
            QUIT_BUTTON = Button.Button(image=None, pos=(380, 550), text_input="MENU", font=button_font, base_color="White", hovering_color="Green")
            QUIT_BUTTON.changeColor(PLAY_MOUSE_POS)
            QUIT_BUTTON.update(window)

            # Check for clicks
            for event in pygame.event.get():
                # Press x button to close app
                if event.type == pygame.QUIT:
                    avatar.clear_tickets()
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
                            asteroids.start_asteroids()
                        elif game == "breakout":
                            breakout.start_breakout()
                        elif game == "invader":
                            invader.main()
                            
                        
                    elif QUIT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        running = False

            pygame.display.update()
