
from turtle import Turtle, Screen
from ball import Ball
from pad import Pad

TIMER_DELAY = 5
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400


def move_ball():
    ball.move()


    screen.ontimer(move_ball, TIMER_DELAY)


screen = Screen()
screen.delay(0)

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)


ball = Ball()
pad = Pad()
ball.fd(10)

print(pad.xcor())
print(pad.ycor())


screen.onkey(pad.move_left, 'Left')
screen.onkey(pad.move_right, 'Right')
screen.onkey(move_ball, 'space')
screen.listen()

pad.screen.mainloop()

