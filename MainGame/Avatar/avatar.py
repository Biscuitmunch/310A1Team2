from email.policy import default
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

pygame.init()

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

#Variables
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

global quit_avatar
global current_avatar

font = pygame.font.SysFont('monospace', 40)

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

            #Break if quit button clicked
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_avatar = True
                    break_loops = True
                    pygame.display.set_caption("Arcade Menu")

            self.display.fill('black')
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

        

