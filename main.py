import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random

# speed should be in between 1 to 10
SPEED = 4

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1200, height=800)
screen.title('Pong Game')
screen.tracer(0)
PADDLE_POSITION = 580


paddle_left = Paddle(-PADDLE_POSITION-5, 0)

paddle_right = Paddle(PADDLE_POSITION, 0)


board_right = Scoreboard((-60, 300))

board_left = Scoreboard((60, 300))


line = Scoreboard((0, -500))
ball = Ball()
game_on = True


def game():
    """main execution of the game"""
    global game_on
    # initial scores of the players
    board_left.board_update(0)
    board_right.board_update(0)
    player_left_score = 0
    player_right_score = 0
    # making the middle line
    line.clear()
    line.goto(0, -500)
    line.setheading(90)
    line.pendown()
    for _ in range(0, 24):
        line.forward(20)
        line.penup()
        line.forward(20)
        line.pendown()
    ball_collision_allowed = True
    # game loop starts
    while game_on:
        # controlling the speed of the ball
        speed = .1 - ball.moving_speed / 100
        # game over sequence
        if speed < 0:
            line.penup()
            line.home()
            line.write('Speed Limit crosses the upper bound', False, "center", ("Arial", 40, 'normal'))
            game_on = False
            break
        screen.update()
        time.sleep(speed)
        ball.forward(20)
        # insuring double collision with bat shouldn't happen
        # maximum angle can be 33 degree for making collision with the other bat -
        # - if ball left the other corner for direct collision calculated by tangent of (screen.width/screen.height)
        if ball.heading() in range(0, 33) or ball.heading() in range(303, 360) or 147 < ball.heading() < 213:
            ball_collision_allowed = True
        if ball_collision_allowed:
            if PADDLE_POSITION + 10 > abs(round(ball.xcor())) > PADDLE_POSITION - 10:
                if ball.distance(paddle_left) < 70 or ball.distance(paddle_right) < 70:
                    ball.colliding_with_paddle()
                    # multiple collision with bat not allowed
                    ball_collision_allowed = False
            # can be executed freely
            # checking if ball crosses the boundary
            elif abs(round(ball.xcor())) > PADDLE_POSITION:
                # ball is missed by left player
                if ball.xcor() > 0:
                    player_right_score += 1
                    board_right.board_update(player_right_score)
                    ball.home()
                    ball.setheading(random.randint(100, 260))
                # ball is missed by right player
                else:
                    ball.home()
                    ball.setheading(random.randint(-80, 80))
                    player_left_score += 1
                    board_left.board_update(player_left_score)
                # Game 0ver sequence
                if player_right_score > 10 or player_left_score > 10:
                    line.penup()
                    line.home()
                    line.write('Game  Over', False, "center", ("Arial", 40, 'normal'))
                    game_on = False
                    break
        # ball collision with wall
        if round(ball.ycor()) > 370 or round(ball.ycor()) < -370:
            ball.colliding_with_wall()
            # if ball collided with the wall then it is allowed to collide with the bats again
            ball_collision_allowed = True


def start_again():
    """to start the entire game again"""
    global game_on
    game_on = True
    ball.home()
    ball.moving_speed = ball.initial_speed
    ball.setheading(random.randint(0, 360))
    game()


def exit_game():
    """to stop the while loop"""
    global game_on
    game_on = False


screen.listen()

screen.onkey(paddle_left.move_up, "Up")
screen.onkey(paddle_left.move_down, "Down")

screen.onkey(paddle_right.move_up, "w")
screen.onkey(paddle_right.move_down, "s")

screen.onkey(start_again, "c")
screen.onkey(exit_game, "e")
screen.exitonclick()
