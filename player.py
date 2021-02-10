from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def reset_player(self):
        self.goto(0, -280)

    def move_up(self):
        """Move player up"""
        self.goto(self.xcor(), self.ycor() + 10)

    def move_down(self):
        """Move player down"""
        self.goto(self.xcor(), self.ycor() - 10)

    def move_right(self):
        """Move player right"""
        self.goto(self.xcor() + 10, self.ycor())

    def move_left(self):
        """Move player left"""
        self.goto(self.xcor() - 10, self.ycor())
