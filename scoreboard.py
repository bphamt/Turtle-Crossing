from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(-260, 270)
        self.pendown()
        self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 10, "bold"))

    def update_score(self):
        """Update Scoreboard on top right of game"""
        self.score += 1
        self.clear()
        self.goto(-260, 270)
        self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 10, "bold"))

    def game_over(self):
        """Reset score to 0 if car hits player"""
        self.score = 0
        self.clear()
        self.goto(-260, 270)
        self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 10, "bold"))




