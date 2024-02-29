import time
from turtle import Turtle, Screen
from ball import Ball
from pad import Pad
from block_matrix import BlockMatrix

TIMER_DELAY = 2  # milliseconds
SLEEP_TIME = 0.001  # seconds
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

screen_max_x = SCREEN_WIDTH / 2
screen_max_y = SCREEN_HEIGHT / 2


def move_ball():
    while True:
        pad.move(screen_max_x)
        ball.move(screen_max_x, screen_max_y, pad, block_matrix)
        screen.update()
        time.sleep(SLEEP_TIME)

    # screen.ontimer(move_ball, TIMER_DELAY)


if __name__ == "__main__":
    screen = Screen()
    screen.delay(0)
    screen.tracer(False)

    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

    ball = Ball()
    pad = Pad()
    block_matrix = BlockMatrix(100)


    screen.onkeypress(lambda: pad.set_left(True), 'Left')
    screen.onkeypress(lambda: pad.set_right(True), 'Right')
    screen.onkeyrelease(lambda: pad.set_left(False), 'Left')
    screen.onkeyrelease(lambda: pad.set_right(False), 'Right')
    screen.listen()
    screen.update()

    move_ball()
    screen.mainloop()
