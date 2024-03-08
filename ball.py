import time
from pad import Pad
from my_turtle import MyTurtle
from block_matrix import BlockMatrix

MAX_BOUNCE_DIRECTION_TILT = 70  # degrees from pad


def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


class Ball(MyTurtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.setheading(90)

    def move_to_pad(self, pad: Pad):
        x = pad.xcor()
        y = pad.ycor() + pad.get_correct_strech()[0] * 10 + self.get_correct_strech()[0] * 10
        self.setposition(x, y)

    def change_direction(self, collision_direction: str):
        """
        change direction of the ball depending on which side of it collided
        :param collision_direction: which side of the ball was colliding with the wall? left, right, up, bottom
        """
        new_heading = 0
        heading = self.heading()

        match collision_direction:
            case 'right':
                if 90 > heading >= 0:
                    new_heading = 180 - heading
                elif 270 < heading < 360:
                    new_heading = 180 + abs(360 - heading)
            case 'up':
                if 90 >= heading > 0:
                    new_heading = 270 + abs(90 - heading)
                elif 90 < heading < 180:
                    new_heading = 270 - abs(90 - heading)
            case 'left':
                if 180 >= heading > 90:
                    new_heading = 0 + abs(180 - heading)
                elif 180 < heading < 270:
                    new_heading = 360 - abs(180 - heading)
            case 'down':
                if 270 >= heading > 180:
                    new_heading = 90 + abs(270 - heading)
                elif 270 < heading < 360:
                    new_heading = 90 - abs(270 - heading)
        self.setheading(new_heading)

    def move(self, screen_max_x, screen_max_y, pad: Pad, block_matrix: BlockMatrix):
        """
        moves a ball one pixel forward, detects collisions, and changes direction if needed
        :param screen_max_x:
        :param screen_max_y:
        :param pad:
        :param block_matrix:
        :return: True - move completed successfully, False - ball collided with bottom ball
        """
        self.fd(1)

        # check collision with screen borders
        if self.right_x() >= screen_max_x:
            self.change_direction("right")
        if self.top_y() >= screen_max_y:
            self.change_direction("up")
        if self.left_x() <= -screen_max_x:
            self.change_direction("left")
        # game over if touches bottom of the screen
        if self.bottom_y() <= -screen_max_y:
            return False

        # check collision with pad
        if (180 < self.heading() < 360 and self.bottom_y() < pad.top_y() and self.right_x() > pad.left_x()
                and self.left_x() < pad.right_x() and self.ycor() > pad.ycor()):
            # if you change ball stretch, function becomes incorrect
            new_direction = map_range(self.xcor(), pad.left_x() - 10, pad.right_x() + 10,
                                      90 + MAX_BOUNCE_DIRECTION_TILT, 90 - MAX_BOUNCE_DIRECTION_TILT)
            self.setheading(new_direction)

        # check collision with blocks
        block_matrix.sort_by_distance(self.xcor(), self.ycor())
        for block in block_matrix.blocks:
            if block.isvisible():

                # check collision with left side of the block
                if ((270 < self.heading() <= 360 or 0 <= self.heading() < 90)
                        and self.right_x() >= block.left_x() and self.bottom_y() < block.top_y()
                        and self.top_y() > block.bottom_y() and self.xcor() < block.left_x()
                        and abs(self.right_x() - block.left_x()) < abs(self.top_y() - block.bottom_y())
                        and abs(self.right_x() - block.left_x()) < abs(self.bottom_y() - block.top_y())):
                    block.hideturtle()
                    self.change_direction('right')

                # check collision with right side of the block
                elif (90 < self.heading() < 270
                      and self.bottom_y() < block.top_y() and self.top_y() > block.bottom_y()
                      and self.left_x() <= block.right_x() and self.xcor() > block.right_x()
                      and abs(self.left_x() - block.right_x()) < abs(self.top_y() - block.bottom_y())
                      and abs(self.left_x() - block.right_x()) < abs(self.bottom_y() - block.top_y())):
                    block.hideturtle()
                    self.change_direction('left')

                # check collision with top side of the block
                elif (180 < self.heading() < 360
                      and self.right_x() > block.left_x() and self.left_x() < block.right_x()
                      and self.bottom_y() <= block.top_y() and self.ycor() > block.top_y()):
                    block.hideturtle()
                    self.change_direction('down')

                # check collision with bottom side of the block
                elif (0 < self.heading() < 180
                      and self.right_x() > block.left_x() and self.left_x() < block.right_x()
                      and self.top_y() >= block.bottom_y() and self.ycor() < block.bottom_y()):
                    block.hideturtle()
                    self.change_direction('up')

        return True

