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
PLAYER_SPEED = 3
ENEMY_SPEED = 2

font = pygame.font.SysFont('arial', 25)

clock = pygame.time.Clock()
fps = 60

class PongGame:

    def __init__(self, width = WINDOW_WIDTH, height = WINDOW_HEIGHT):
        pygame.display.set_caption("Pong")
        self.width = width
        self.height = height
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
        if enemy1.y > ball.y:
            enemy1.top = enemy1.top - ENEMY_SPEED
            enemy1.bottom = enemy1.bottom - ENEMY_SPEED

        elif enemy1.y < ball.y:
            enemy1.top = enemy1.top + ENEMY_SPEED
            enemy1.bottom = enemy1.bottom + ENEMY_SPEED

    def ball_movement(self, ball):
        # Variables needed
        global ball_velocity_x
        global ball_velocity_y
        global player1
        global game_over
        global enemy1
        ball.x = ball.x + ball_velocity_x
        ball.y = ball.y + ball_velocity_y

        # Conditions when the ball hits a screen edge
        if ball.right >= WINDOW_WIDTH:
            print("player scores")
            game_over = True
        if ball.left <= 0:
            print("bot scores")
            game_over = True
        if ball.bottom >= WINDOW_HEIGHT or ball.top <= 0:
            ball_velocity_y = -ball_velocity_y
        
        # Hitting player now
        if ball.x == player1.x + PADDLE_WIDTH/2 and ball.bottom >= player1.bottom and ball.top >= player1.top:
            ball_velocity_x = -ball_velocity_x

    def start_game(self):
        global break_loops
        global game_over
        global ball_velocity_x
        global ball_velocity_y
        global player1
        global enemy1
        global ball
        break_loops = False
        game_over = False
        ball_velocity_x = -5
        ball_velocity_y = 5
        
        player1 = pygame.Rect(80, WINDOW_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
        enemy1 = pygame.Rect(WINDOW_WIDTH-80, WINDOW_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
        ball = pygame.Rect(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, BALL_RADIUS, BALL_RADIUS)

        while game_over == False:
            self.player_movement(player1)
            self.ball_movement(ball)
            self.enemy_movement(enemy1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    break_loops = True
                    pygame.display.set_caption("Arcade Menu")

            self.display.fill('black')
            pygame.draw.rect(self.display, 'white', player1)
            pygame.draw.rect(self.display, 'white', enemy1)
            pygame.draw.circle(self.display, 'white', ball.center, BALL_RADIUS)
            pygame.display.update()
            clock.tick(fps)
