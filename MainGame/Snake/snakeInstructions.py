import pygame
import Snake.snake as snake
import sys

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
        while True:            
            window = pygame.display.set_mode((WIDTH, HEIGHT))
            window.fill("black")
            font = pygame.font.SysFont('arial', 25)

            play_image_un = pygame.image.load(
                "MainGame/Buttons/PlayUnpressedButton.png").convert_alpha()
            play_image_pressed = pygame.image.load(
                "MainGame/Buttons/PlayPressedButton.png").convert_alpha()
            quit_image_un = pygame.image.load(
                "MainGame/Buttons/QuitUnpressedButton.png").convert_alpha()
            quit_image_pressed = pygame.image.load(
                "MainGame/Buttons/QuitPressedButton.png").convert_alpha()

            play = ScreenItem(0, 0, play_image_un)
            quit = ScreenItem(WIDTH - 100, HEIGHT - 100, quit_image_un)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for event in pygame.event.get():
                
                # User tried to click:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play.mouse_over_button(pygame.mouse.get_pos()):
                        snake_obj = snake.snake_game()
                        snake_obj.start_game()
                        
                    elif quit.mouse_over_button(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
                    

                #Detect mouse hovering
                if event.type == pygame.MOUSEMOTION:
                    # Activate Snake
                    if play.mouse_over_button(pygame.mouse.get_pos()):
                        play = ScreenItem(WIDTH/2, HEIGHT/2, play_image_pressed)
                    
                    #Activate Avatar Select
                    elif quit.mouse_over_button(pygame.mouse.get_pos()):
                        quit = ScreenItem(WIDTH/2, HEIGHT/2, quit_image_pressed)


            # Show buttons on screen
            play.update()
            quit.update()
            
            pygame.display.update()
