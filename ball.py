from turtle import Turtle
import random

MOVE = 10
DIRECTIONS = [45, 135, 225, 315]

class Ball:

    def __init__(self):
        self.ball = Turtle("circle")
        self.ball.color("white")
        self.ball.speed(1)
        self.ball.penup()


    def ball_direction(self):
        self.ball.setheading(random.choice(DIRECTIONS))

    def ball_move(self):
        self.ball.forward(MOVE)

    def wall(self):
        if  self.ball.ycor() > 390 and self.ball.xcor() > 0:
            self.ball.setheading(self.ball.heading() - 90)
        elif self.ball.ycor() > 390 and self.ball.xcor() < 0:
            self.ball.setheading(self.ball.heading() + 90)
        elif self.ball.ycor() < -390 and self.ball.xcor() > 0:
            self.ball.setheading(self.ball.heading() - 90)
        elif self.ball.ycor() < -390 and self.ball.xcor() < 0:
            self.ball.setheading(self.ball.heading() + 90)

    def position(self):
        return self.ball.position()
