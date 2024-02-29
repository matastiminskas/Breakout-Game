from my_turtle import MyTurtle
import numpy as np

STRETCH_X = 2
STRETCH_Y = 1
LINES = 5
COLUMNS = 10
SPACING_X = 5
SPACING_Y = 5


class BlockMatrix:
    def __init__(self, center_y):
        total_x = (COLUMNS - 1) * (SPACING_X + 20 * STRETCH_X) # between centers of left and right blocks
        total_y = (LINES - 1) * (SPACING_Y + 20 * STRETCH_Y) # between centers of top and bottom blocks
        self.blocks = []
        half_x = total_x / 2
        half_y = total_y / 2

        for x in np.linspace(-half_x, half_x, COLUMNS):
            for y in np.linspace(center_y - half_y, center_y + half_y, LINES):
                block = MyTurtle()
                block.shape("square")
                block.turtlesize(STRETCH_Y, STRETCH_X)
                block.goto(x, y)
                self.blocks.append(block)

