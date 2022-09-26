# PyArcade

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-360/) 

PyArcade is a game made in python that can support and let you play many different arcade games that you may have seen or played at some point. 

PyArcade is developed by SOFTENG 310 Team 2 and SOFTENG 310 Team 5 From University of Auckland

Any new suggestions or changes are welcome to help expand the arcades library!&nbsp;&nbsp; [Contributing.](#contribution)



## Menu
  - [🕹️ GAMES](#%EF%B8%8F-games)
    - [🐍 Snake](#-snake)
    - [🧱 Breakout](#-breakout)
    - [🏓 Pong](#-pong)
    - [👾 Invader](#-invader)
    - [🚀 Asteroids](#-asteroids)

## Installation
To run the arcade, you will need to have python3 installed, as well as pygame.

Pygame can be installed by simply using the pip script 
```
pip install pygame
```
Running the MainMenu.py file from the root directory should now open the arcade.
```
py MainGame/main_menu.py
```

## Test Environment

Test suite requires pytest.
```
pip3 install pytest
```
<br>
<br>


<h2 align='center'>🕹️ Games</h2>

## 🐍 Snake 
<p>
The player navigates a snake through the map, attempts to eat items by running into them with the head of the snake. Each item eaten makes the snake longer, avoiding collision with the snake body and map border
</p>

![snakeImage](https://user-images.githubusercontent.com/79783194/192203501-601e0d36-3e83-463d-a412-e507aef0327d.png)

## 🧱 Breakout
<p>
Breakout begins with rows of bricks, with different kinds of color. The color order from the bottom up is green, blue and red. Using a single ball, the player must knock down as many bricks as possible by using the walls and/or the paddle below to hit the ball against the bricks and eliminate them. If the player's paddle misses the ball's rebound, they will lose. Power items will be granted, with two different powerups, extra ball and a power ball.
</p>

![image](https://user-images.githubusercontent.com/79783194/192204569-ee90986a-62fb-49d0-83f4-9ca7eedb9771.png)


## 🏓 Pong
<p>
Pong is a two-dimensional sports game that simulates table tennis. The player controls an in-game paddle by moving it vertically across the left side of the screen. The user will compete the AI player controlling a second paddle on the right side. Players use the paddles to hit a ball back and forth. The goal for player is to reach highest points before the opponent earn five points; points are earned when one fails to return the ball to the other.
</p>

![image](https://user-images.githubusercontent.com/79783194/192205045-c08a9ee4-0302-4022-a6aa-e90afc8293d5.png)

## 👾 Space Invader
<p>
Space Invaders is a fixed shooter in which the player moves a laser cannon horizontally and verically across the screen and fires at aliens overhead. The goal is to eliminate all of the aliens by shooting them. While the player has a health bar, player will lose health hit by the aliens. If the invaders reach the bottom of the screen, lives will drop by one, the player has five lives in total, the game ends when the player lives reach 0.
</p>

![image](https://user-images.githubusercontent.com/79783194/192205838-5031e3f9-6ab4-4ee7-99f9-41f2ccb8da50.png)

## 🚀 Asteroids
<p>
The objective of Asteroids is to destroy asteroids. The player controls a triangular ship that can rotate left and right, fire shots straight forward, and thrust forward. Scores are earned when hits asterorids.
</p>

![image](https://user-images.githubusercontent.com/79783194/192207603-3ce24e4f-6659-450a-8491-88084c298a04.png)

## Contribution
PyArcade is developed by SOFTENG 310 Team 2 for Assignment 1 and take over by SOFTENG 310 Team 5 for Assignment 2

Detailed contribution please reference to the [Wiki](https://github.com/Biscuitmunch/310A1Team2/wiki) pages [list of contribution].(https://github.com/Biscuitmunch/310A1Team2/wiki/List-of-Contributions)

Want to contribute to the repository? Check out our [Contributing guidelines](./CONTRIBUTING.md)!

## Licensing

PyArcade and it's contributions are licensed under MIT
