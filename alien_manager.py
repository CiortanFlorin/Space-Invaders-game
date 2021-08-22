from turtle import Turtle



class AlienManager(Turtle):

    def __init__(self, x, y):
        super(). __init__()
        self.speed("fastest")
        self.shape("turtle")
        self.penup()
        self.shapesize(2, 2, 1)
        self.color("white")
        self.seth(270)
        self.goto(x,y)
        self.x = x
        self.y = y

    def move(self):
        self.x += 10
        self.goto(self.x, self.y)