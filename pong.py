__author__ = 'MaxZhuang'
# import cs1lib
from cs1lib import *

# declare constants
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
WINDOW_TOP_Y = 0  # highest point on the screen
WINDOW_LEFT_X = 0  # furthest point left on the screen
PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20
STARTING_PADDLE_X1 = 0  # starting X value of paddle 1
STARTING_PADDLE_Y1 = 0  # starting Y value of paddle 1
STARTING_PADDLE_X2 = 380  # starting X value of paddle 2
STARTING_PADDLE_Y2 = 320  # starting Y value of paddle 2
PADDLE_MOVE = 10  # pixels of how much paddles move
NAP_DURATION = .02  # time for sleep function
STARTING_BALL_X = 200  # starting x position of ball, center
STARTING_BALL_Y = 200  # starting y position of ball, center
RADIUS_BALL = 10
BOUNCE = -1  # factor to reverse direction of ball when making contact
STOP_GAME = 0  # speed of ball when you "stop the game"
BALL_MOVE = 3  # how many pixels it is moving
RED = .8  # color of red used for paddle
RED_SHADE_G = .2  # color of green used for red color of paddle
BLACK = 0  # color of black used in coloring
WHITE = 1  # color white for ball


# function to determine contact with paddle 1
def contact_paddle_1(x_ball, y_ball, paddle_y1):
    return y_ball >= paddle_y1 and y_ball <= paddle_y1 + PADDLE_HEIGHT and x_ball - RADIUS_BALL <= STARTING_PADDLE_X1 + PADDLE_WIDTH

# function to determine contact with paddle 2
def contact_paddle_2(x_ball, y_ball, paddle_y2):
    return y_ball >= paddle_y2 and y_ball <= paddle_y2 + PADDLE_HEIGHT and x_ball + RADIUS_BALL >= STARTING_PADDLE_X2

# function to determine contact with the top wall
def contact_top_wall(y_ball):
   return y_ball - RADIUS_BALL <= WINDOW_TOP_Y

# function to determine contact with the bottom wall
def contact_bottom_wall(y_ball):
  return y_ball + RADIUS_BALL >= WINDOW_HEIGHT

# function to determine contact with the right wall
def contact_right_wall(x_ball):
    return x_ball + RADIUS_BALL >= WINDOW_WIDTH

# function to determine contact with the left wall
def contact_left_wall(x_ball):
    return x_ball - RADIUS_BALL <= WINDOW_LEFT_X


# main function
def graphics_window():

    # sets background
    set_clear_color(BLACK, BLACK, BLACK)
    clear()
    disable_stroke()

    # variables for movement of paddles
    moving_y1 = STARTING_PADDLE_Y1  # set initial y coordinate of paddle 1
    moving_y2 = STARTING_PADDLE_Y2  # set initial y coordinate of paddle 2

    # variables for movement of ball
    ball_x = STARTING_BALL_X  # set position of ball in x direction
    ball_y = STARTING_BALL_Y  # set position of ball in y direction
    ball_x_velocity = BALL_MOVE  # sets initial x velocity of ball
    ball_y_velocity = BALL_MOVE  # sets initial y velocity of ball


    # while loop for main game function
    while not window_closed():

        # draws paddles
        set_fill_color(RED, RED_SHADE_G, BLACK)
        draw_rectangle(STARTING_PADDLE_X1, moving_y1, PADDLE_WIDTH, PADDLE_HEIGHT)
        draw_rectangle(STARTING_PADDLE_X2, moving_y2, PADDLE_WIDTH, PADDLE_HEIGHT)

        # if statements that move y coordinates of paddles
        if is_key_pressed("a") and moving_y1 > STARTING_PADDLE_Y1:
            moving_y1 = moving_y1 - PADDLE_MOVE

        if is_key_pressed("z") and moving_y1 < STARTING_PADDLE_Y2:
            moving_y1 = moving_y1 + PADDLE_MOVE

        if is_key_pressed("k") and moving_y2 > STARTING_PADDLE_Y1:
            moving_y2 = moving_y2 - PADDLE_MOVE

        if is_key_pressed("m") and moving_y2 < STARTING_PADDLE_Y2:
            moving_y2 = moving_y2 + PADDLE_MOVE

        # if statements for reset and quit game
        if is_key_pressed(" "):
            moving_y1 = STARTING_PADDLE_Y1  # reset to original y coordinate of paddle 1
            moving_y2 = STARTING_PADDLE_Y2  # reset to original y coordinate of paddle 2
            ball_x = STARTING_BALL_X  # reset to original ball x
            ball_y = STARTING_BALL_Y  # reset to original ball y
            ball_x_velocity = BALL_MOVE
            ball_y_velocity = BALL_MOVE
            request_redraw()
            clear()

        if is_key_pressed("q"):
            cs1_quit()

        # draws ball
        set_fill_color(WHITE, WHITE, WHITE)
        draw_circle(ball_x, ball_y, RADIUS_BALL)

        # sets initial direction ball moves
        ball_x = ball_x + ball_x_velocity
        ball_y = ball_y + ball_y_velocity

        # if statements call contact functions, pass variables, change direction of ball
        if contact_paddle_1(ball_x, ball_y, moving_y1):
            ball_x_velocity = BALL_MOVE

        if contact_paddle_2(ball_x, ball_y, moving_y2):
            ball_x_velocity = ball_x_velocity * BOUNCE

        if contact_top_wall(ball_y):
            ball_y_velocity = BALL_MOVE

        if contact_bottom_wall(ball_y):
            ball_y_velocity = ball_y_velocity * BOUNCE

        # if statements call contact functions, pass variables, end the game
        if contact_right_wall(ball_x):
            ball_x_velocity = STOP_GAME
            ball_y_velocity = STOP_GAME
            ball_x = STARTING_BALL_X
            ball_y = STARTING_BALL_Y

        if contact_left_wall(ball_x):
            ball_x_velocity = STOP_GAME
            ball_y_velocity = STOP_GAME
            ball_x = STARTING_BALL_X
            ball_y = STARTING_BALL_Y

        # redraw, slow graphics, clear screen
        request_redraw()
        sleep(NAP_DURATION)
        clear()

# starts graphics
start_graphics(graphics_window, "PONG!", WINDOW_HEIGHT, WINDOW_WIDTH)