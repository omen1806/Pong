from turtle import Turtle

STARTING_POSITION = [
    [(680, 40), (680, 20), (680, 00), (680, -20), (680, -40)],
    [(-680, 40), (-680, 20), (-680, 00), (-680, -20), (-680, -40)]
]
MOVE = 40

class Paddle:

    def __init__(self):
        self.paddle = []

    def create_paddle(self, number):
        for position in STARTING_POSITION[number - 1]:
            element = Turtle("square")
            element.color("white")
            element.speed(50)
            element.penup()
            element.goto(position)
            self.paddle.append(element)

    def move_up(self):
        for element in self.paddle:
            element.setheading(90)
            element.forward(MOVE)

    def move_down(self):
        for element in self.paddle:
            element.backward(MOVE)

    def check_collision(self, ball_position):
        for element in self.paddle:
            if element.distance(ball_position) < 10:
                print("collision")



