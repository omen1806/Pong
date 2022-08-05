from turtle import Turtle

class Score_2:

    def __init__(self):
        self.score = 0
        self.ele = Turtle()
        self.ele.penup()
        self.ele.hideturtle()
        self.ele.goto(-60, 260)
        self.ele.pencolor("white")
        self.ele.write("0", True, "center", ("Courier", 90, "normal"))

    def score_up_2(self):
        self.ele.clear()
        self.ele.goto(-60, 260)
        self.score += 1
        self.ele.write(self.score, True, "center", ("Courier", 90, "normal"))
