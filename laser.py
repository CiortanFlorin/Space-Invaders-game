from turtle import Turtle


class Laser(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.shapesize(0.1, 1.2, 1)
        self.color("white")
        self.goto(0, 320)
        self.setheading(90)

    def advance(self):
        self.forward(30)