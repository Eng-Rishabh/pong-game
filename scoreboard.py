from turtle import Turtle
FONT = ("Courier", 100, 'normal')


class Scoreboard(Turtle):
    def __init__(self, position):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)

    def board_update(self, score):
        self.clear()
        self.write(score, False, "center", FONT)
