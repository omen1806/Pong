from turtle import Turtle

STARTING_POSITION = [
    [(680, 0), (680, 20), (680, 40), (680, -20), (680, -40)],
    [(-680, 0), (-680, 20), (-680, 40), (-680, -20), (-680, -40)]
]

class Paddle(Turtle):

    def __init__(self):
        pass

    def get_paddle(self, number):
        for position in STARTING_POSITION[number-1]:
            self.paddle = Turtle("square")
            self.paddle.color("white")
            self.paddle.speed(50)
            self.paddle.penup()
            self.paddle.goto(position)

    def paddle_up(self):
        for i in

