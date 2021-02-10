from turtle import Turtle
import random
CAR_LIST = []
COLOR_LIST = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
POSITION = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLOR_LIST))
        CAR_LIST.append(self)
        self.goto(260, 0)

    def car_starting_point(self):
        """Set car to starting position from random position list"""
        self.goto(260, (random.choice(POSITION)))

    def move(self):
        """Move car forward 10 pixel"""
        for i in CAR_LIST:
            i.backward(10)

    def detect_collison(self, player):
        """Detect if car hits player"""
        for car in CAR_LIST:
            if car.distance(player) < 20:
                return True

    def delete_car(self):
        """Delete car object (in theory, doesn't seem to work much in Turtle graphics)"""
        for self in CAR_LIST:
            if self.xcor() < -300:
                del self