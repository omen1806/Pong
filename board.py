from turtle import Turtle, Screen

class Board(Turtle):

    def __init__(self):
        self.board = Turtle()
        self.board.speed(50)
        self.board.color("white")
        self.board.penup()
        self.board.goto(0, 400)
        self.board.right(90)
        self.board.pensize(5)

    def draw_board(self):
        for i in range(20):
            self.board.pendown()
            self.board.forward(20)
            self.board.penup()
            self.board.forward(20)



