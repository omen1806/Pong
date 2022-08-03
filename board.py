from turtle import Turtle, Screen

class Board(Turtle):

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.goto(0, 400)
        self.turtle.right(90)
        self.turtle.pensize(5)

    def draw_board(self):
        for i in range(20):
            self.turtle.pendown()
            self.turtle.forward(20)
            self.turtle.penup()
            self.turtle.forward(20)



