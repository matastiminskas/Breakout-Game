from turtle import Turtle


class MyTurtle(Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.penup()
        self.speed(0)

    def get_correct_strech(self):
        """
        :return: (stretch_y, stretch_x, outline)
        """
        if self.heading() == 0 or self.turtlesize()[0] == self.turtlesize()[1]:
            return self.turtlesize()
        else:
            heading = self.heading()
            self.setheading(0)
            stretch = self.turtlesize()
            self.setheading(heading)
            return stretch

    def left_x(self):
        strech_x = self.get_correct_strech()[1]
        return self.xcor() - 20 * strech_x / 2


    def right_x(self):
        strech_x = self.get_correct_strech()[1]
        return self.xcor() + 20 * strech_x / 2

    def top_y(self):
        strech_y = self.get_correct_strech()[0]
        return self.ycor() + 20 * strech_y / 2

    def bottom_y(self):
        strech_y = self.get_correct_strech()[0]
        return self.ycor() - 20 * strech_y / 2