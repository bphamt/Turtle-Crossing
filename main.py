from turtle import Screen
from player import Player
from board import Board
from car import Car
from scoreboard import Scoreboard
import time
import random

GAME_STATE = True

# Screen Setup
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()

# Player object
player = Player()

# Board object
starting_line = Board(0, -260)
finish_line = Board(0, 260)
score = Scoreboard()

# Car object, Generate 200 for starting
for i in range(200):
     car = Car()
car.car_starting_point()

# Inputs
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_down, key="Down")
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=player.move_right, key="Right")

while GAME_STATE:
    time.sleep(0.02)
    screen.update()

    # Generate random number for car generation
    new_car_random = random.randint(0, 2)

    # Delete car if reaches the left end
    car.delete_car()

    # If player hits car
    if car.detect_collison(player):
        player.reset_player()
        score.game_over()

    # Player Scores
    if player.ycor() > 240:
        print("score")
        score.update_score()
        player.reset_player()

    # Generate new car if random int is 0
    if new_car_random == 0:
        car = Car()
        car.car_starting_point()

    # Move car
    car.move()
