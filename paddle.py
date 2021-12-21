from turtle import Turtle
COLOR = 'White'
PADDLE_STEP = 40


class Paddle(Turtle):
    def __init__(self, x, y):
        super(Paddle, self).__init__()
        self.hideturtle()
        self.penup()
        self.color(COLOR)
        self.shape('square')
        self.shapesize(1, 7)
        self.setheading(90)
        self.goto(x, y)
        self.showturtle()

    def move_up(self):
        new_y = self.ycor() + PADDLE_STEP
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - PADDLE_STEP
        self.goto(self.xcor(), new_y)
