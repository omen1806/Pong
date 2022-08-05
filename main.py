from turtle import Screen
from paddle import Paddle
from board import Board
from ball import Ball
from score import Score
from score_2 import Score_2

import time

MOVING_SPEED = 0.001

game_is_on = True

# CREATING BACKGROUND
screen = Screen()
screen.setup(1400, 800, 250, 100)
screen.bgcolor("black")
screen.title("PONG")
board = Board()
board.draw_board()

score = Score()
score_2 = Score_2()

# CREATING PADDLES
paddle_1 = Paddle()
paddle_1.create_paddle(1)
paddle_2 = Paddle()
paddle_2.create_paddle(2)

# PADDLES MOVING
screen.listen()
screen.onkey(paddle_1.move_up, 'Up')
screen.onkey(paddle_2.move_up, 'w')
screen.onkey(paddle_1.move_down, 'Down')
screen.onkey(paddle_2.move_down, 's')


# GAME IN PROGRESS
while game_is_on:
    ball_ok = True
    screen.update()
    screen.tracer(0)
    ball = Ball()
    ball.ball_direction()
    while ball_ok:
        screen.update()
        screen.tracer(0)
        ball.ball_move()
        time.sleep(MOVING_SPEED)
        ball.wall_up_down()
        if paddle_1.check_collision(ball.position()) or paddle_2.check_collision(ball.position()):
            ball.ball_on_paddle()
        elif ball.wall_right():
            score_2.score_up_2()
            ball_ok = False
        elif ball.wall_left():
            score.score_up()
            ball_ok = False











screen.exitonclick()
