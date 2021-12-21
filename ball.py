import random
from turtle import Turtle
# Should be in between 1 to 9
INITIAL_SPEED = 2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.initial_speed = INITIAL_SPEED
        self.hideturtle()
        self.penup()
        self.color("yellow")
        self.shape('circle')
        self.speed("fastest")
        self.showturtle()
        self.setheading(random.randint(0, 360))
        self.moving_speed = INITIAL_SPEED

    # we can also do this by playing with x and y coordinate but it will not be so general
    # but can be made general
    def colliding_with_paddle(self):
        # for right bat collision
        if self.heading() < 91:
            self.setheading(random.randint(100, 260))
        elif self.heading() > 270:
            self.setheading(random.randint(100, 260))
        # for left bat collision
        elif self.heading() in range(90, 271):
            if random.getrandbits(1):
                self.setheading(random.randint(0, 81))
            else:
                self.setheading(random.randint(280, 360))
        self.moving_speed += .1

    def colliding_with_wall(self):
        # ball collide with upper surface
        if self.heading() < 181:
            self.setheading(270 + (90 - self.heading()))
        # ball collide with lower surface
        else:
            self.setheading(90 + (270 - self.heading()))
