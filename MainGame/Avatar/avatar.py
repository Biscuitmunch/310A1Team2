from email.policy import default
from os import environ
from turtle import Screen
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

pygame.init()

# Scale variables
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
AVATAR_SIZE = 100, 100

global quit_avatar
global current_avatar

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.SysFont('monospace', 40)

# Class to load items that can be displayed and interacted with
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


# Open image files for avatar graphics and scale to size
default_avatar = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/defaultAvatar.png'), (AVATAR_SIZE))
avatar1 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar1.png'), (AVATAR_SIZE))
avatar2 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar2.png'), (AVATAR_SIZE))
avatar3 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar3.png'), (AVATAR_SIZE))
avatar4 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar4.png'), (AVATAR_SIZE))
avatar5 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar5.png'), (AVATAR_SIZE))
avatar6 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar6.png'), (AVATAR_SIZE))
avatar7 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar5.png'), (AVATAR_SIZE))
avatar8 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar3.png'), (AVATAR_SIZE))
arrow = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/arrow.png'), (AVATAR_SIZE))

current_avatar = default_avatar

class AvatarSelect:

    def __init__(self, width = WINDOW_WIDTH, height = WINDOW_HEIGHT):
        pygame.display.set_caption("Avatar Select")
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
    
    def get_current_avatar(self):
        global current_avatar
        return current_avatar
    
    def start_selection(self):
        global current_avatar
        global quit_avatar
        break_loops = False

        current_avatar = default_avatar
        temp_avatar = current_avatar
        temp_avatar_hide = True
        quit_avatar = False

        while quit_avatar == False and break_loops == False:

            # Handling user behaviour and interactions
            for event in pygame.event.get():
                # Quits avatar select
                if event.type == pygame.QUIT:
                    quit_avatar = True
                    break_loops = True
                    pygame.display.set_caption("Arcade Menu")

                # Looks for user clicking on different avatars
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if avatar_1_Button.mouse_over_button(pygame.mouse.get_pos()):
                        current_avatar = avatar1
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
                        current_avatar = default_avatar

                # Looks for user hovering on different avatars
                if event.type == pygame.MOUSEMOTION:
                    if avatar_1_Button.mouse_over_button(pygame.mouse.get_pos()):
                        temp_avatar = avatar1
                        temp_avatar_hide = False
                    elif avatar_2_Button.mouse_over_button(pygame.mouse.get_pos()):
                        temp_avatar = avatar2
                        temp_avatar_hide = False
                    elif avatar_3_Button.mouse_over_button(pygame.mouse.get_pos()):
                        temp_avatar = avatar3
                        temp_avatar_hide = False
                    elif avatar_4_Button.mouse_over_button(pygame.mouse.get_pos()):
                        temp_avatar = avatar4
                        temp_avatar_hide = False
                    elif avatar_5_Button.mouse_over_button(pygame.mouse.get_pos()):
                        temp_avatar = avatar5
                        temp_avatar_hide = False
                    elif avatar_6_Button.mouse_over_button(pygame.mouse.get_pos()):
                        temp_avatar = avatar6
                        temp_avatar_hide = False
                    elif avatar_7_Button.mouse_over_button(pygame.mouse.get_pos()):
                        temp_avatar = avatar7
                        temp_avatar_hide = False
                    elif avatar_8_Button.mouse_over_button(pygame.mouse.get_pos()):
                        temp_avatar = default_avatar
                        temp_avatar_hide = False
                    else:
                        temp_avatar_hide = True

            self.display.fill('black')

            # Set positions for avatar images
            current_avatar_display = ScreenItem(WINDOW_WIDTH/2-100, 80, current_avatar)
            avatar_1_Button = ScreenItem(100,350,avatar1)
            avatar_2_Button = ScreenItem(250,350,avatar2)
            avatar_3_Button = ScreenItem(400,350,avatar3)
            avatar_4_Button = ScreenItem(550,350,avatar4)
            avatar_5_Button = ScreenItem(700,350,avatar5)
            avatar_6_Button = ScreenItem(850,350,avatar6)
            avatar_7_Button = ScreenItem(1000,350,avatar7)
            avatar_8_Button = ScreenItem(1150,350,default_avatar)
            temp_avatar_button = ScreenItem(WINDOW_WIDTH/2+100, 80, temp_avatar)
            window.blit(arrow, (WINDOW_WIDTH/2-50, 100))

            # Display avatars on screen
            current_avatar_display.update()
            avatar_1_Button.update()
            avatar_2_Button.update()
            avatar_3_Button.update()
            avatar_4_Button.update()
            avatar_5_Button.update()
            avatar_6_Button.update()
            avatar_7_Button.update()
            avatar_8_Button.update()

            if temp_avatar_hide == False:
                temp_avatar_button.update()

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

        

