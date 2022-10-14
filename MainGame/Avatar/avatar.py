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
global tickets

# Starter tickets and avatars
tickets = 100
avatar_1_redeemed = True
avatar_2_redeemed = False
avatar_3_redeemed = False
avatar_4_redeemed = False
avatar_5_redeemed = False
avatar_6_redeemed = False
avatar_7_redeemed = False
avatar_8_redeemed = False


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.SysFont('monospace', 40)

# Open image files and scale to size
avatar1 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar1.png'), (AVATAR_SIZE))
avatar2 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar2.png'), (AVATAR_SIZE))
avatar3 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar3.png'), (AVATAR_SIZE))
avatar4 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar4.png'), (AVATAR_SIZE))
avatar5 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar5.png'), (AVATAR_SIZE))
avatar6 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar6.png'), (AVATAR_SIZE))
avatar7 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar7.png'), (AVATAR_SIZE))
avatar8 = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/avatar8.png'), (AVATAR_SIZE))
arrow = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/arrow.png'), (AVATAR_SIZE))
lock = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/lock.png'), (AVATAR_SIZE))
back = pygame.transform.scale(pygame.image.load('MainGame/Avatar/resources/back.png'), (150, 80))

current_avatar = avatar1

class AvatarSelect:

    def __init__(self, width = WINDOW_WIDTH, height = WINDOW_HEIGHT):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
    
    def get_current_avatar(self):
        global current_avatar
        return current_avatar
    
    def get_tickets(self):
        global tickets
        return tickets
 
    def start_selection(self):
        from main_menu import ScreenItem
        pygame.display.set_caption("Avatar Select")
        global current_avatar
        global quit_avatar
        global tickets
        global avatar_1_redeemed
        global avatar_2_redeemed
        global avatar_3_redeemed
        global avatar_4_redeemed
        global avatar_5_redeemed
        global avatar_6_redeemed
        global avatar_7_redeemed
        global avatar_8_redeemed
        break_loops = False
        
        # Hide text by default
        ticket_text_show = False
        ticket_title = font.render(" ", True, (255, 255, 255))
        ticket_text = ScreenItem(100, 400, ticket_title)

        temp_avatar = current_avatar
        temp_avatar_hide = True
        quit_avatar = False

        
        

        while quit_avatar == False and break_loops == False:

            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            QUIT_BUTTON = Button.Button(image=None, pos=(125, 70), text_input="MENU", font=button_font, base_color="White", hovering_color="Green")
            QUIT_BUTTON.changeColor(PLAY_MOUSE_POS)
            QUIT_BUTTON.update(window)

            # Handling user behaviour and interactions
            for event in pygame.event.get():
                # Quits avatar select
                if event.type == pygame.QUIT:
                    quit_avatar = True
                    break_loops = True
                    pygame.display.set_caption('Arcade Menu')

                # Looks for user clicking on different avatars
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if avatar_1_button.mouse_over_button(pygame.mouse.get_pos()):
                        #avatar 1 is redeemed by default
                        current_avatar = avatar1
                    elif avatar_2_button.mouse_over_button(pygame.mouse.get_pos()):
                        if avatar_2_redeemed == True:
                            current_avatar = avatar2
                        elif avatar_2_redeemed == False:
                            if tickets >= 50:
                                avatar_2_redeemed = True
                                tickets = tickets - 50
                                current_avatar = avatar2
                    elif avatar_3_button.mouse_over_button(pygame.mouse.get_pos()):
                        if avatar_3_redeemed == True:
                            current_avatar = avatar3
                        elif avatar_3_redeemed == False:
                            if tickets >= 50:
                                avatar_3_redeemed = True
                                tickets = tickets - 50
                                current_avatar = avatar3
                    elif avatar_4_button.mouse_over_button(pygame.mouse.get_pos()):
                        if avatar_4_redeemed == True:
                            current_avatar = avatar4
                        elif avatar_4_redeemed == False:
                            if tickets >= 50:
                                avatar_4_redeemed = True
                                tickets = tickets - 50
                                current_avatar = avatar4
                    elif avatar_5_button.mouse_over_button(pygame.mouse.get_pos()):
                        if avatar_5_redeemed == True:
                            current_avatar = avatar5
                        elif avatar_5_redeemed == False:
                            if tickets >= 100:
                                avatar_5_redeemed = True
                                tickets = tickets - 100
                                current_avatar = avatar5
                    elif avatar_6_button.mouse_over_button(pygame.mouse.get_pos()):
                        if avatar_6_redeemed == True:
                            current_avatar = avatar6
                        elif avatar_6_redeemed == False:
                            if tickets >= 100:
                                avatar_6_redeemed = True
                                tickets = tickets - 100
                                current_avatar = avatar6
                    elif avatar_7_button.mouse_over_button(pygame.mouse.get_pos()):
                        if avatar_7_redeemed == True:
                            current_avatar = avatar7
                        elif avatar_7_redeemed == False:
                            if tickets >= 100:
                                avatar_7_redeemed = True
                                tickets = tickets - 100
                                current_avatar = avatar7
                    elif avatar_8_button.mouse_over_button(pygame.mouse.get_pos()):
                        if avatar_8_redeemed == True:
                            current_avatar = avatar8
                        elif avatar_8_redeemed == False:
                            if tickets >= 150:
                                avatar_8_redeemed = True
                                tickets = tickets - 150
                                current_avatar = avatar8

                # Looks for user hovering on different avatars
                if event.type == pygame.MOUSEMOTION:
                    if avatar_1_button.mouse_over_button(pygame.mouse.get_pos()):
                        ticket_text_show = True
                        ticket_title = font.render("equip", True, 'white')
                        ticket_text = ScreenItem(100, 420, ticket_title)
                        #avatar 1 is redeemed by default
                        temp_avatar = avatar1
                        temp_avatar_hide = False
                    elif avatar_2_button.mouse_over_button(pygame.mouse.get_pos()):
                        ticket_text_show = True
                        if avatar_2_redeemed == True:
                            ticket_title = font.render("equip", True, 'white')
                            temp_avatar = avatar2
                            temp_avatar_hide = False
                        else:
                            temp_avatar = lock
                            temp_avatar_hide = False
                            if tickets >= 50:
                                ticket_title = font.render("50", True, 'white')
                            else:
                                ticket_title = font.render("50", True, 'red')
                        ticket_text = ScreenItem(250, 420, ticket_title)
                    elif avatar_3_button.mouse_over_button(pygame.mouse.get_pos()):
                        ticket_text_show = True
                        if avatar_3_redeemed == True:
                            ticket_title = font.render("equip", True, 'white')
                            temp_avatar = avatar3
                            temp_avatar_hide = False
                        else:
                            temp_avatar = lock
                            temp_avatar_hide = False
                            if tickets >= 50:
                                ticket_title = font.render("50", True, 'white')
                            else:
                                ticket_title = font.render("50", True, 'red')
                        ticket_text = ScreenItem(400, 420, ticket_title)
                    elif avatar_4_button.mouse_over_button(pygame.mouse.get_pos()):
                        ticket_text_show = True
                        if avatar_4_redeemed == True:
                            ticket_title = font.render("equip", True, 'white')
                            temp_avatar = avatar3
                            temp_avatar_hide = False
                        else:
                            temp_avatar = lock
                            temp_avatar_hide = False
                            if tickets >= 50:
                                ticket_title = font.render("50", True, 'white')
                            else:
                                ticket_title = font.render("50", True, 'red')
                        ticket_text = ScreenItem(550, 420, ticket_title)
                    elif avatar_5_button.mouse_over_button(pygame.mouse.get_pos()):
                        ticket_text_show = True
                        if avatar_5_redeemed == True:
                            ticket_title = font.render("equip", True, 'white')
                            temp_avatar = avatar3
                            temp_avatar_hide = False
                        else:
                            temp_avatar = lock
                            temp_avatar_hide = False
                            if tickets >= 100:
                                ticket_title = font.render("100", True, 'white')
                            else:
                                ticket_title = font.render("100", True, 'red')
                        ticket_text = ScreenItem(700, 420, ticket_title)
                    elif avatar_6_button.mouse_over_button(pygame.mouse.get_pos()):
                        ticket_text_show = True
                        if avatar_6_redeemed == True:
                            ticket_title = font.render("equip", True, 'white')
                            temp_avatar = avatar3
                            temp_avatar_hide = False
                        else:
                            temp_avatar = lock
                            temp_avatar_hide = False
                            if tickets >= 100:
                                ticket_title = font.render("100", True, 'white')
                            else:
                                ticket_title = font.render("100", True, 'red')
                        ticket_text = ScreenItem(850, 420, ticket_title)
                    elif avatar_7_button.mouse_over_button(pygame.mouse.get_pos()):
                        ticket_text_show = True
                        if avatar_7_redeemed == True:
                            ticket_title = font.render("equip", True, 'white')
                            temp_avatar = avatar3
                            temp_avatar_hide = False
                        else:
                            temp_avatar = lock
                            temp_avatar_hide = False
                            if tickets >= 100:
                                ticket_title = font.render("100", True, 'white')
                            else:
                                ticket_title = font.render("100", True, 'red')
                        ticket_text = ScreenItem(1000, 420, ticket_title)
                    elif avatar_8_button.mouse_over_button(pygame.mouse.get_pos()):
                        ticket_text_show = True
                        if avatar_8_redeemed == True:
                            ticket_title = font.render("equip", True, 'white')
                            temp_avatar = avatar3
                            temp_avatar_hide = False
                        else:
                            temp_avatar = lock
                            temp_avatar_hide = False
                            if tickets >= 150:
                                ticket_title = font.render("150", True, 'white')
                            else:
                                ticket_title = font.render("150", True, 'red')
                        ticket_text = ScreenItem(1150, 420, ticket_title)
                    else:
                        temp_avatar_hide = True
                        ticket_text_show = False

            self.display.fill('black')

            # Set positions for images
            current_avatar_display = ScreenItem(WINDOW_WIDTH/2-100, 80, current_avatar)
            avatar_1_button = ScreenItem(100,350,avatar1)
            avatar_2_button = ScreenItem(250,350,avatar2)
            avatar_3_button = ScreenItem(400,350,avatar3)
            avatar_4_button = ScreenItem(550,350,avatar4)
            avatar_5_button = ScreenItem(700,350,avatar5)
            avatar_6_button = ScreenItem(850,350,avatar6)
            avatar_7_button = ScreenItem(1000,350,avatar7)
            avatar_8_button = ScreenItem(1150,350,avatar8)
            temp_avatar_button = ScreenItem(WINDOW_WIDTH/2+100, 80, temp_avatar)
            window.blit(arrow, (WINDOW_WIDTH/2-50, 100))
            return_button = ScreenItem(1100, 80, back)

            # Display images on screen
            current_avatar_display.update()
            avatar_1_button.update()
            avatar_2_button.update()
            avatar_3_button.update()
            avatar_4_button.update()
            avatar_5_button.update()
            avatar_6_button.update()
            avatar_7_button.update()
            avatar_8_button.update()
            return_button.update()

            # Display text
            message = font.render("Choose your avatar!", True, 'white')
            ticket_display = font.render("Tickets:" + str(tickets), True, 'white')
            message_obj = ScreenItem(WINDOW_WIDTH/2, 500, message)
            ticket_display_obj = ScreenItem(WINDOW_WIDTH/2, 550, ticket_display)
            message_obj.update()
            ticket_display_obj.update()

            if temp_avatar_hide == False:
                temp_avatar_button.update()

            if ticket_text_show == True:
                ticket_text.update()

            if ticket_text_show == True:
                ticket_text.update()

            pygame.display.update()
        
        # Return to main menu
        while quit_avatar == True and break_loops == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_avatar = True
                    break_loops = True
                    pygame.display.set_caption('Arcade Menu')
                    
            self.display.fill('black')
            pygame.display.update()

        

