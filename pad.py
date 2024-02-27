from turtle import Turtle

MOVE_DISTANCE = 10 # per keypress
STRETCH_X = 3
STRETCH_Y = 0.5
DISTANCE_FROM_BOTTOM = 40

class Pad(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.penup()
        self.turtlesize(stretch_wid=STRETCH_Y, stretch_len=STRETCH_X)
        print(self.screen.window_height())
        self.sety(-self.screen.window_height() / 2 + DISTANCE_FROM_BOTTOM)

    def move_left(self):
        self.setx(self.xcor() - MOVE_DISTANCE)

    def move_right(self):
        self.setx(self.xcor() + MOVE_DISTANCE)

    def left_x(self):
        return self.xcor() - 20 * STRETCH_X / 2

    def right_x(self):
        return self.xcor() + 20 * STRETCH_X / 2

    def top_y(self):
        return self.xcor() - 20 * STRETCH_Y / 2


