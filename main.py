import time
from turtle import Turtle, Screen
from ball import Ball
from pad import Pad
from block_matrix import BlockMatrix

SLEEP_TIME = 0.005  # seconds between moves
SCREEN_UPDATE_DELAY = 0.030  # seconds between screen updates
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

screen_max_x = SCREEN_WIDTH / 2
screen_max_y = SCREEN_HEIGHT / 2
last_update_time = time.perf_counter()

game_stage = 'new_game'  # new_game, play, game_over, game_won


def print_on_screen(text: str):
    turtle = Turtle()
    turtle.penup()
    turtle.hideturtle()
    turtle.write(text, align='center', font=('Arial', 20, 'normal'))


def move_ball():
    global game_stage
    global last_update_time
    while True:
        move_start_time = time.perf_counter()

        # start = time.perf_counter()
        pad.move(screen_max_x)
        if game_stage == 'new_game':
            ball.move_to_pad(pad)
        elif game_stage == 'play':
            if not ball.move(screen_max_x, screen_max_y, pad, block_matrix):
                game_stage = 'game_over'
            if block_matrix.all_blocks_hidden():
                game_stage = 'game_won'
        # print(time.perf_counter() - start)
        elif game_stage == 'game_won':
            print_on_screen('game won')
            break
        elif game_stage == 'game_over':
            print_on_screen('game over')
            break

        current_time = time.perf_counter()
        if current_time - last_update_time >= SCREEN_UPDATE_DELAY:
            last_update_time = current_time
            screen.update()

        move_end_time = time.perf_counter()
        # screen.update takes a lot of time with many blocks, so we try to compensate
        # with decreasing sleep time between moves
        if move_end_time - move_start_time < SLEEP_TIME:
            time.sleep(SLEEP_TIME - (move_end_time - move_start_time))

    screen.update()


def start_game():
    # start a game once and remove space button binding
    global game_stage
    game_stage = 'play'
    screen.onkeyrelease(None, 'space')


if __name__ == "__main__":
    screen = Screen()
    screen.delay(0)
    screen.tracer(False)

    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

    ball = Ball()
    pad = Pad()
    block_matrix = BlockMatrix(80)



    screen.onkeypress(lambda: pad.set_left(True), 'Left')
    screen.onkeypress(lambda: pad.set_right(True), 'Right')
    screen.onkeyrelease(lambda: pad.set_left(False), 'Left')
    screen.onkeyrelease(lambda: pad.set_right(False), 'Right')
    screen.onkeyrelease(start_game, 'space')
    screen.listen()
    screen.update()

    move_ball()
    screen.mainloop()
