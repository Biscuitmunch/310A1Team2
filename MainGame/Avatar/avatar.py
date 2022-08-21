from email.policy import default
from os import environ
from turtle import Screen
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

pygame.init()

#Variables
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

global quit_avatar
global current_avatar

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.SysFont('monospace', 40)

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


# Open image files for avatar graphics - files will change when art implemented
default_avatar = pygame.image.load('MainGame/Avatar/resources/defaultAvatar.png')
avatar1 = pygame.image.load('MainGame/Avatar/resources/testAvatar.png')
avatar2 = pygame.image.load('MainGame/Avatar/resources/defaultAvatar.png')
avatar3 = pygame.image.load('MainGame/Avatar/resources/defaultAvatar.png')
avatar4 = pygame.image.load('MainGame/Avatar/resources/defaultAvatar.png')
avatar5 = pygame.image.load('MainGame/Avatar/resources/defaultAvatar.png')
avatar6 = pygame.image.load('MainGame/Avatar/resources/defaultAvatar.png')
# Locked avatars below
avatar7 = pygame.image.load('MainGame/Avatar/resources/defaultAvatar.png')
avatar8 = pygame.image.load('MainGame/Avatar/resources/defaultAvatar.png')
avatar9 = pygame.image.load('MainGame/Avatar/resources/defaultAvatar.png')
avatar10 = pygame.image.load('MainGame/Avatar/resources/defaultAvatar.png')

class AvatarSelect:

    def __init__(self, width = WINDOW_WIDTH, height = WINDOW_HEIGHT):
        pygame.display.set_caption("Avatar Select")
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
    
    
    def choose_avatar(self, chosen_avatar):
        current_avatar = chosen_avatar



    def start_selection(self):
        global current_avatar
        global quit_avatar
        break_loops = False

        current_avatar = default_avatar
        quit_avatar = False

        while quit_avatar == False and break_loops == False:

            # User behaviour
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_avatar = True
                    break_loops = True
                    pygame.display.set_caption("Arcade Menu")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if avatar_1_Button.mouse_over_button(pygame.mouse.get_pos()):
                        current_avatar = default_avatar
                    elif avatar_2_Button.mouse_over_button(pygame.mouse.get_pos()):
                        current_avatar = avatar2
                    elif avatar_3_Button.mouse_over_button(pygame.mouse.get_pos()):
                        current_avatar = avatar3
                    elif avatar_4_Button.mouse_over_button(pygame.mouse.get_pos()):
                        current_avatar = avatar4
                    elif avatar_5_Button.mouse_over_button(pygame.mouse.get_pos()):
                        current_avatar = avatar5
                    elif avatar_6_Button.mouse_over_button(pygame.mouse.get_pos()):
                        current_avatar = avatar6
                    elif avatar_7_Button.mouse_over_button(pygame.mouse.get_pos()):
                        current_avatar = avatar7
                    elif avatar_8_Button.mouse_over_button(pygame.mouse.get_pos()):
                        current_avatar = avatar1
                        pygame.display.update()

            self.display.fill('black')

            # Set positions for avatar images
            current_avatar_display = ScreenItem(WINDOW_WIDTH/2-50, 80, current_avatar)
            avatar_1_Button = ScreenItem(100,350,default_avatar)
            avatar_2_Button = ScreenItem(250,350,avatar2)
            avatar_3_Button = ScreenItem(400,350,avatar3)
            avatar_4_Button = ScreenItem(550,350,avatar4)
            avatar_5_Button = ScreenItem(700,350,avatar5)
            avatar_6_Button = ScreenItem(850,350,avatar6)
            avatar_7_Button = ScreenItem(1000,350,avatar7)
            avatar_8_Button = ScreenItem(1150,350,avatar1)

            # Display avatars as buttons
            current_avatar_display.update()
            avatar_1_Button.update()
            avatar_2_Button.update()
            avatar_3_Button.update()
            avatar_4_Button.update()
            avatar_5_Button.update()
            avatar_6_Button.update()
            avatar_7_Button.update()
            avatar_8_Button.update()
            pygame.display.update()
        
        # Return to main menu
        while quit_avatar == True and break_loops == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_avatar = True
                    break_loops = True
                    pygame.display.set_caption("Arcade Menu")
                    
            self.display.fill('black')
            pygame.display.update()

        

