from turtle import Screen
import pygame
import sys
import Snake.snake as snake
import Instructions as Instructions
import Pong.pong as pong
import Avatar.avatar as avatar
import Invader.space_invaders as invader
import Asteroids.asteroids as asteroids 
import Scoreboard.Scoreboard as Scoreboard
import Breakout.breakout as Breakout
import Buttons.InstrucButton as button

WIDTH = 1280
HEIGHT = 720

window = pygame.display.set_mode((WIDTH, HEIGHT))
caption_title = pygame.display.set_caption("Arcade Menu")
pygame.init()

# Class to display items such as text and images as clickable/hideable/showable objects on screen
class ScreenItem():
    def __init__(self, x, y, image):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))

    # Show the item
    def update(self):
        window.blit(self.image, self.rect)

    # Determine if mouse is interacting with item to perform further logic
    def mouse_over_button(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True

font = pygame.font.SysFont('arial', 25)


# Load Main Menu Images
title_image = pygame.image.load(
    "MainGame/Buttons/title.png").convert_alpha()
player_text_image = pygame.transform.scale(pygame.image.load(
    "MainGame/Buttons/player.png").convert_alpha(), (150,25))
snake_image = pygame.image.load(
    "MainGame/Buttons/SnakeButton.png").convert_alpha()
breakout_image = pygame.image.load(
    "MainGame/Buttons/BreakoutButton.png").convert_alpha()
pong_image = pygame.image.load(
    "MainGame/Buttons/PongButton.png").convert_alpha()
invader_image = pygame.image.load(
    "MainGame/Buttons/InvadersButton.png").convert_alpha()
asteroids_image = pygame.image.load( 
    "MainGame/Buttons/AsteroidsButton.png").convert_alpha()
scoreboard_image = pygame.image.load(
    "MainGame/Buttons/ScoresButton.png").convert_alpha()


# Main Menu text items
play_title = font.render("Click to Play!", True, 'white')
avatar_select_title = font.render("Select Avatar!", True, 'white')
play_text = ScreenItem(0, 0, play_title)
avatar_text = ScreenItem(0, 0, avatar_select_title)

# Main Menu Buttons
title = ScreenItem(WIDTH/2, 80, title_image)
player_text = ScreenItem(WIDTH - 150, 140, player_text_image)
snake_button = ScreenItem(263.67, 540, snake_image)
breakout_button = ScreenItem(657.54, 540, breakout_image)
pong_button = ScreenItem (1051.41, 540, pong_image)
invader_button = ScreenItem(263.67, 300, invader_image)
asteroids_button = ScreenItem (657.54, 300, asteroids_image)
scoreboard_button = ScreenItem(1051, 300, scoreboard_image)



# Hide text by default
play_text_show = False
avatar_text_show = False

# Show text on call of these functions
def set_play_text(button):
    play_text.x = button.x
    play_text.y = button.y + 120
    play_text.rect = play_text.image.get_rect(center=(play_text.x, play_text.y))

def set_avatar_text(button):
    avatar_text.x = button.x
    avatar_text.y = button.y + 100
    avatar_text.rect = avatar_text.image.get_rect(center=(avatar_text.x, avatar_text.y))

# Main Menu Loop
running = True
while running:
    pygame.display.set_caption("Arcade Menu")
    PLAY_MOUSE_POS = pygame.mouse.get_pos()
    button_font = pygame.font.Font("MainGame/Fonts/PressStart2P.ttf", 35)
    quit_button = button.Button(image=None, pos=(155, 85), text_input="QUIT", font=button_font, base_color="White", hovering_color="Green")

   

    # Initialize Avatar
    avatar_obj = avatar.AvatarSelect()
    avatar_image = avatar_obj.get_current_avatar()
    avatar_button = ScreenItem(WIDTH - 150, 70, pygame.transform.scale(avatar_image, (80,80)))

    for event in pygame.event.get():
        

        # To exit the game
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

        # User tried to click:
        # Quit Arcade
        if event.type == pygame.MOUSEBUTTONDOWN:
            if quit_button.checkForInput(PLAY_MOUSE_POS):
                pygame.display.quit()
                sys.exit()
                
            # Activate Avatar Select
            elif avatar_button.mouse_over_button(pygame.mouse.get_pos()):
                avatar_obj = avatar.AvatarSelect()
                avatar_obj.start_selection()

            # Activate Snake
            elif snake_button.mouse_over_button(pygame.mouse.get_pos()):
                Instructions.instructions().play("snake")

            # Activate Breakout
            elif breakout_button.mouse_over_button(pygame.mouse.get_pos()):
                Instructions.instructions().play("breakout")

            # Activate Pong
            elif pong_button.mouse_over_button(pygame.mouse.get_pos()):
                Instructions.instructions().play("pong")

             # Activate Space Invaders
            elif invader_button.mouse_over_button(pygame.mouse.get_pos()):
                Instructions.instructions().play("invader")

            # Activate Asteroids
            elif asteroids_button.mouse_over_button(pygame.mouse.get_pos()):
                Instructions.instructions().play("asteroids")

            # Activate Scoreboard
            elif scoreboard_button.mouse_over_button(pygame.mouse.get_pos()):
                Scoreboard.startScoreboard()

        # Detect mouse hovering
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
            
            # Activate Invaders
            elif invader_button.mouse_over_button(pygame.mouse.get_pos()):
                set_play_text(invader_button)
                play_text_show = True

             # Activate asteroids
            elif asteroids_button.mouse_over_button(pygame.mouse.get_pos()):
                set_play_text(asteroids_button)
                play_text_show = True

            elif scoreboard_button.mouse_over_button(pygame.mouse.get_pos()):
                set_play_text(scoreboard_button)
                play_text_show = True

            # If user is doing nothing
            else:
                play_text_show = False
                avatar_text_show = False

    window.fill("black")

    # Show buttons on screen
    title.update()
    player_text.update()
    avatar_button.update()
    snake_button.update()
    breakout_button.update()
    pong_button.update()
    invader_button.update()
    asteroids_button.update()
    scoreboard_button.update()
    quit_button.changeColor(PLAY_MOUSE_POS)
    quit_button.update(window)
    
    

    # Display Text logic
    if play_text_show == True:
        play_text.update()
    
    if avatar_text_show == True:
        avatar_text.update()


    pygame.display.update()

pygame.display.quit()