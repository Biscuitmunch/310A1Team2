from os import environ
from tkinter import CENTER
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import random
import math
from enum import Enum
from collections import namedtuple

pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
PADDLE_WIDTH = 8
PADDLE_HEIGHT = 90
BALL_RADIUS = 8
PLAYER_SPEED = 3.7
ENEMY_SPEED = 3.3

font = pygame.font.SysFont('monospace', 40)

clock = pygame.time.Clock()
fps = 60

class PongGame:

    def __init__(self, width = WINDOW_WIDTH, height = WINDOW_HEIGHT):
        pygame.display.set_caption("Pong")
        self.width = width
        self.height = height
        self.score_player = 0
        self.score_enemy = 0
        self.display = pygame.display.set_mode((self.width, self.height))

    def player_movement(self, player1):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and player1.top > 0:
            player1.top = player1.top - PLAYER_SPEED
            player1.bottom = player1.bottom - PLAYER_SPEED

        if keys[pygame.K_DOWN] and player1.bottom < 720:
            player1.top = player1.top + PLAYER_SPEED
            player1.bottom = player1.bottom + PLAYER_SPEED

    def enemy_movement(self, enemy1):
        global ball
        if enemy1.y > ball.y and enemy1.top > 0:
            enemy1.top = enemy1.top - ENEMY_SPEED
            enemy1.bottom = enemy1.bottom - ENEMY_SPEED

        elif enemy1.y < ball.y and enemy1.bottom < 720:
            enemy1.top = enemy1.top + ENEMY_SPEED
            enemy1.bottom = enemy1.bottom + ENEMY_SPEED

    def reset_ball(self, ball):
        global next_paddle
        global ball_velocity_x
        global ball_velocity_y
        next_paddle = 'player'
        ball_velocity_x = -5
        ball_velocity_y = random.choice([5, -5])

        ball.x = WINDOW_WIDTH/2
        ball.y = WINDOW_WIDTH/2

    def ball_movement(self, ball):
        # Variables needed
        global ball_velocity_x
        global ball_velocity_y
        global player1
        global game_over
        global enemy1
        global next_paddle
        ball.x = ball.x + ball_velocity_x
        ball.y = ball.y + ball_velocity_y

        # Conditions when the ball hits a screen edge
        if ball.right >= WINDOW_WIDTH:
            self.score_player = self.score_player + 1
            self.reset_ball(ball)
            
        if ball.left <= 0:
            self.score_enemy = self.score_enemy + 1
            self.reset_ball(ball)

        if ball.bottom >= WINDOW_HEIGHT or ball.top <= 0:
            ball_velocity_y = -ball_velocity_y

        # Paddle collisions
        if ball.colliderect(player1) and next_paddle == 'player':
            if ball_velocity_y < 0:
                ball_velocity_y = ball_velocity_y - 0.3
            else:
                ball_velocity_y = ball_velocity_y + 0.3
            ball_velocity_x = ball_velocity_x - random.random()
            ball_velocity_x = -ball_velocity_x
            next_paddle = 'enemy'

        if ball.colliderect(enemy1) and next_paddle == 'enemy':
            if ball_velocity_y < 0:
                ball_velocity_y = ball_velocity_y - 0.3
            else:
                ball_velocity_y = ball_velocity_y + 0.3
            ball_velocity_x = ball_velocity_x + random.random()
            ball_velocity_x = -ball_velocity_x
            next_paddle = 'player'

    def start_game(self):
        global break_loops
        global game_over
        global ball_velocity_x
        global ball_velocity_y
        global player1
        global enemy1
        global ball
        global next_paddle
        next_paddle = 'player'
        break_loops = False
        game_over = False
        ball_velocity_x = -5
        ball_velocity_y = 5
        
        player1 = pygame.Rect(80, WINDOW_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
        enemy1 = pygame.Rect(WINDOW_WIDTH-80, WINDOW_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
        ball = pygame.Rect(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, BALL_RADIUS, BALL_RADIUS)

        while game_over == False and break_loops == False:
            self.player_movement(player1)
            self.ball_movement(ball)
            self.enemy_movement(enemy1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    break_loops = True
                    pygame.display.set_caption("Arcade Menu")

            self.display.fill('black')
            score_text = font.render(str(self.score_player) + "   ---   " + str(self.score_enemy), True, 'white')
            self.display.blit(score_text, [WINDOW_WIDTH/2 - 100, 0])
            pygame.draw.rect(self.display, 'white', player1)
            pygame.draw.rect(self.display, 'white', enemy1)
            pygame.draw.circle(self.display, 'white', ball.center, BALL_RADIUS)
            pygame.display.update()
            clock.tick(fps)

        while game_over == True and break_loops == False:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    break_loops = True
                    pygame.display.set_caption("Arcade Menu")
                    
            self.display.fill('black')
            pygame.display.update()
            clock.tick(fps)


