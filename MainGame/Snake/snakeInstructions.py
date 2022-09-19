import pygame
import Snake.snake as snake
import sys
import Buttons.InstrucButton as Button

WIDTH = 1280
HEIGHT = 720

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

    def play(self):
        running = True
        while running:            
            window = pygame.display.set_mode((WIDTH, HEIGHT))
            window.fill("black")
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            font = pygame.font.Font("MainGame/Buttons/PressStart2P.ttf", 25)
            title_font = pygame.font.Font("MainGame/Buttons/PressStart2P.ttf", 50)
            button_font = pygame.font.Font("MainGame/Buttons/PressStart2P.ttf", 35)

            # Game title
            PLAY_TEXT = title_font.render("SNAKE", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 200))
            window.blit(PLAY_TEXT, PLAY_RECT)

            # Instructions (3 lines)
            INSTRUC_TEXT_1 = font.render("use arrow keys to change directions", True, "White")
            INSTRUC_RECT_1 = INSTRUC_TEXT_1.get_rect(center=(640, 300))
            window.blit(INSTRUC_TEXT_1, INSTRUC_RECT_1)
            INSTRUC_TEXT_2 = font.render("don’t run into any walls or your own tail", True, "White")
            INSTRUC_RECT_2 = INSTRUC_TEXT_2.get_rect(center=(640, 350))
            window.blit(INSTRUC_TEXT_2, INSTRUC_RECT_2)
            INSTRUC_TEXT_3 = font.render("eat cherries to grow", True, "White")
            INSTRUC_RECT_3 = INSTRUC_TEXT_3.get_rect(center=(640, 400))
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
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        snake_obj = snake.snake_game()
                        snake_obj.start_game()
                    elif QUIT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        running = False

            pygame.display.update()
