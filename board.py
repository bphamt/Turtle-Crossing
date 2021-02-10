from turtle import Turtle


class Board(Turtle):
    def __init__(self, x, y):
        super().__init__()

        self.x_cor = x
        self.y_cor = y
        self.speed("fastest")
        self.penup()
        self.goto(self.x_cor - 300, self.y_cor)
        self.pendown()

        if self.y_cor == -260:
            self.color("green")
        else:
            self.color("red")

        self.forward(800)

