class TestGamesLinked:
    
    # To make sure your game is being imported, add it same as the other tests here

    # Snake
    def test_snake(self):
        try:
            import Snake.snake as snake
        except ImportError as import_error:
            print(import_error)
            print("Snake failed to import!")
        except Exception as e:
            print(e)
            print("Bug in snake.py!")
        else:
            print("Successfully implemented Snake")

    # Breakout
    def test_breakout(self):
        try:
            import Breakout.breakout as breakout
        except ImportError as import_error:
            print(import_error)
            print("Breakout failed to import!")
        except Exception as e:
            print(e)
            print("Bug in breakout.py!")
        else:
            print("Successfully implemented Breakout")

    # Pong
    def test_pong(self):
        try:
            import Pong.pong as pong
        except ImportError as import_error:
            print(import_error)
            print("Pong failed to import!")
        except Exception as e:
            print(e)
            print("Bug in pong.py!")
        else:
            print("Successfully implemented Pong!")

    # Invaders
    def test_invaders(self):
        try:
            import Invader.space_invaders as invaders
        except ImportError as import_error:
            print(import_error)
            print("Space Invaders failed to import!")
        except Exception as e:
            print(e)
            print("Bug in invaders.py!")
        else:
            print("Successfully implemented Space Invaders!")

    # Asteroids
    def test_asteroids(self):
        try:
            import Asteroids.asteroids as asteroids
        except ImportError as import_error:
            print(import_error)
            print("Asteroids failed to import!")
        except Exception as e:
            print(e)
            print("Bug in asteroids.py!")
        else:
            print("Successfully implemented Asteroids!")

    # Scoreboard
    def test_scoreboard(self):
        try:
            import Scoreboard.Scoreboard as scoreboard
        except ImportError as import_error:
            print(import_error)
            print("Scoreboard failed to import!")
        except Exception as e:
            print(e)
            print("Bug in Scoreboard.py!")
        else:
            print("Successfully implemented Scoreboard!")

    # Avatar
    def test_avatar(self):
        try:
            import Avatar.avatar as avatar
        except ImportError as import_error:
            print(import_error)
            print("Avatar failed to import!")
        except Exception as e:
            print(e)
            print("Bug in avatar.py!")
        else:
            print("Successfully implemented Avatar!")

# Importing each test case causes it to go through the file initializing the variables, as python runs files on imports
# Each test checks the import works in the first place, then goes to a more specialised exception as something in the
# files initialization went wrong, which should be output when the error occurs
print("=====")
TestGamesLinked().test_snake()
print("=====")
TestGamesLinked().test_breakout()
print("=====")
TestGamesLinked().test_pong()
print("=====")
TestGamesLinked().test_invaders()
print("=====")
TestGamesLinked().test_asteroids()
print("=====")
TestGamesLinked().test_scoreboard()
print("=====")
TestGamesLinked().test_avatar()
print("=====")
print("All games open window successfully!")