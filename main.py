from turtle import Turtle, Screen

import paddle
from board import Board
from paddle import Paddle

screen = Screen()
screen.setup(1400, 800, 250, 100)
screen.bgcolor("black")
screen.title("PONG")

turtle = Turtle()
board = Board()
board.draw_board()
paddle.Paddle().get_paddle(1)
paddle.Paddle().get_paddle(2)






screen.exitonclick()
