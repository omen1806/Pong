from turtle import Screen
from paddle import Paddle
from board import Board
from ball import Ball
import time

MOVING_SPEED = 0.03

game_is_on = True
ball_ok = True

# CREATING BACKGROUND
screen = Screen()
screen.setup(1400, 800, 250, 100)
screen.bgcolor("black")
screen.title("PONG")
screen.listen()
board = Board()
board.draw_board()

# CREATING PADDLES
paddle_1 = Paddle()
paddle_1.create_paddle(1)
paddle_2 = Paddle()
paddle_2.create_paddle(2)

# PADDLES MOVING
screen.onkey(paddle_1.move_up, 'Up')
screen.onkey(paddle_2.move_up, 'w')
screen.onkey(paddle_1.move_down, 'Down')
screen.onkey(paddle_2.move_down, 's')

# CREATE A BALL
ball = Ball()
print(ball)

# GAME IN PROGRESS
while game_is_on:
    screen.update()
    screen.tracer(0)
    ball.ball_direction()
    while ball_ok:
        screen.update()
        screen.tracer(0)
        ball.ball_move()
        time.sleep(MOVING_SPEED)
        ball.wall()
        paddle_1.check_collision(ball.position())
        paddle_2.check_collision(ball.position())









screen.exitonclick()
