from turtle import Turtle, Screen
from board import Board

screen = Screen()
screen.setup(1400, 800, 250, 100)
screen.bgcolor("black")
screen.title("PONG")

turtle = Turtle()
board = Board()
board.draw_board()







screen.exitonclick()
