import pygame
import sys
import Snake.snake as snake
import Pong.pong as pong
import Avatar.avatar as avatar
import Avatar.resources as avatars

WIDTH = 1280
HEIGHT = 720

window = pygame.display.set_mode((WIDTH, HEIGHT))
caption_title = pygame.display.set_caption("Arcade Menu")

pygame.init()

class ScreenItem():
    def __init__(self, x, y, image):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        window.blit(self.image, self.rect)

    def mouse_over_button(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True

font = pygame.font.SysFont('arial', 25)

# Game buttons
snake_image = pygame.image.load(
    "MainGame/Buttons/SnakeButton.png").convert_alpha()
breakout_image = pygame.image.load(
    "MainGame/Buttons/BreakoutButton.png").convert_alpha()
pong_image = pygame.image.load(
    "MainGame/Buttons/PongButton.png").convert_alpha()
quit_image = pygame.image.load(
    "MainGame/Buttons/QuitButton.png").convert_alpha()

# Button texts
play_title = font.render("Click to Play!", True, 'white')
avatar_select_title = font.render("Select Avatar!", True, 'white')

play_text = ScreenItem(0, 0, play_title)
avatar_text = ScreenItem(0, 0, avatar_select_title)

quit_button = ScreenItem(1180, 670, quit_image)
snake_button = ScreenItem(263.67, 540, snake_image)
breakout_button = ScreenItem(657.54, 540, breakout_image)
pong_button = ScreenItem (1051.41, 540, pong_image)

play_text_show = False
avatar_text_show = False

def set_play_text(button):
    play_text.x = button.x
    play_text.y = button.y + 120
    play_text.rect = play_text.image.get_rect(center=(play_text.x, play_text.y))

def set_avatar_text(button):
    avatar_text.x = button.x
    avatar_text.y = button.y + 100
    avatar_text.rect = avatar_text.image.get_rect(center=(avatar_text.x, avatar_text.y))

running = True
while running:
    avatar_obj = avatar.AvatarSelect()
    avatar_image = avatar_obj.get_current_avatar()
    avatar_button = ScreenItem(WIDTH/2, 80, avatar_image)

    for event in pygame.event.get():
        # To exit the game
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

        # User tried to click:
        # Quit Arcade
        if event.type == pygame.MOUSEBUTTONDOWN:
            if quit_button.mouse_over_button(pygame.mouse.get_pos()):
                pygame.display.quit()
                sys.exit()
                
            # Activate Avatar Select
            elif avatar_button.mouse_over_button(pygame.mouse.get_pos()):
                avatar_obj = avatar.AvatarSelect()
                avatar_obj.start_selection()

            # Activate Snake
            elif snake_button.mouse_over_button(pygame.mouse.get_pos()):
                snake_obj = snake.snake_game()
                snake_obj.start_game()

            # Activate Breakout
            elif breakout_button.mouse_over_button(pygame.mouse.get_pos()):
                print("breakout clicked")

            # Activate Pong
            elif pong_button.mouse_over_button(pygame.mouse.get_pos()):
                pong_obj = pong.PongGame()
                pong_obj.start_game()

            # No buttons
            else:
                print("no button clicked")

        if event.type == pygame.MOUSEMOTION:
            # Activate Snake
            if snake_button.mouse_over_button(pygame.mouse.get_pos()):
                set_play_text(snake_button)
                play_text_show = True
            
            # Activate Avatar Select
            elif avatar_button.mouse_over_button(pygame.mouse.get_pos()):
                set_avatar_text(avatar_button)
                avatar_text_show = True

            # Activate Breakout
            elif breakout_button.mouse_over_button(pygame.mouse.get_pos()):
                set_play_text(breakout_button)
                play_text_show = True

            # Activate Pong
            elif pong_button.mouse_over_button(pygame.mouse.get_pos()):
                set_play_text(pong_button)
                play_text_show = True

            # If user is doing nothing
            else:
                play_text_show = False
                avatar_text_show = False

    window.fill("black")

    avatar_button.update()
    snake_button.update()
    breakout_button.update()
    pong_button.update()
    quit_button.update()
    
    if play_text_show == True:
        play_text.update()
    
    if avatar_text_show == True:
        avatar_text.update()


    pygame.display.update()

pygame.display.quit()