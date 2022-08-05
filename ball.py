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

    def wall_up_down(self):
        if  self.ball.ycor() > 390 and self.ball.heading() == 135:
            self.ball.setheading(225)
        elif self.ball.ycor() > 390 and self.ball.heading() == 45:
            self.ball.setheading(315)
        elif self.ball.ycor() < -390 and self.ball.heading() == 315:
            self.ball.setheading(45)
        elif self.ball.ycor() < -390 and self.ball.heading() == 225:
            self.ball.setheading(135)

    def wall_right(self):
        if self.ball.xcor() > 710:
            return True

    def wall_left(self):
        if self.ball.xcor() < -710:
            return True

    def position(self):
        return self.ball.position()

    def ball_on_paddle(self):
        if self.ball.xcor() > 665:
            if self.ball.heading() == 45:
                self.ball.setheading(135)
            else:
                self.ball.setheading(225)
        elif self.ball.xcor() < -665:
            if self.ball.heading() == 135:
                self.ball.setheading(45)
            else:
                self.ball.setheading(315)
