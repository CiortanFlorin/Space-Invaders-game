from turtle import Turtle


class AlienLaser(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.shapesize(0.1, 0.8, 1)
        self.color("white")
        self.goto(x, y)
        self.setheading(270)

    def go_on(self):
        self.forward(10)