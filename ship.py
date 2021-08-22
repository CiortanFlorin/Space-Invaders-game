from turtle import Turtle


class Ship(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("triangle")
        self.color("white")
        self.x = 0
        self.goto(0, -250)
        self.setheading(90)

    def move_left(self):
        self.x -=10
        self.goto(self.x, -250)
    def move_right(self):
        self.x += 10
        self.goto(self.x, -250)
