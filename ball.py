from turtle import Turtle

MAX_BOUNCE_DIRECTION_TILT = 70 # degrees

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.setheading(45)
        self.direction = 0

    def move(self):
        self.fd(1)
