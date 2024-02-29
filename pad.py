from my_turtle import MyTurtle

MOVE_DISTANCE = 1 # per keypress
STRETCH_X = 3
STRETCH_Y = 0.5
DISTANCE_FROM_BOTTOM = 40

class Pad(MyTurtle):
    def __init__(self):
        super().__init__(shape='square')
        self.move_left = False
        self.move_right = False
        self.turtlesize(stretch_wid=STRETCH_Y, stretch_len=STRETCH_X)
        self.sety(-self.screen.window_height() / 2 + DISTANCE_FROM_BOTTOM)

    def set_left(self, value: bool):
        self.move_left = value

    def set_right(self, value: bool):
        self.move_right = value

    def move(self, screen_max_x):
        if self.move_left and not self.move_right and self.left_x() >= -screen_max_x:
            self.setx(self.xcor() - MOVE_DISTANCE)
        elif not self.move_left and self.move_right and self.right_x() <= screen_max_x:
            self.setx(self.xcor() + MOVE_DISTANCE)
