from turtle import Screen, Turtle
import time

from ball import Ball
# from scoreboard import Scoreboard
from paddle import Paddle
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Pong Game2")
screen.tracer(0)
# Create the two players and place them at the left and right edges of the screen.
right_player = Paddle(screen_width=SCREEN_WIDTH / 2 - 30, screen_height=SCREEN_HEIGHT)
left_player = Paddle(screen_width=-SCREEN_WIDTH / 2 + 30, screen_height=SCREEN_HEIGHT)
ball = Ball()
scoreboard = Scoreboard()

# Create screen listening to up and down movements.
screen.listen()
screen.onkeypress(right_player.go_up, "Up")
screen.onkeypress(right_player.go_down, "Down")
screen.onkeypress(left_player.go_up, "w")
screen.onkeypress(left_player.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # Updates the screen manually because screen.tracer is off.
    ball.move()  # Start constant movement of the ball.
    # Detect ball collision with top and bottom walls.
    if ball.ycor() > (SCREEN_HEIGHT / 2) - 20 or ball.ycor() < -(SCREEN_HEIGHT / 2) + 30:
        ball.bounce_y()
    # Handle ball is out of left and right walls.
    if ball.xcor() > (SCREEN_WIDTH / 2):
        # PLAYER 2 GETS A POINT
        ball.reset_position()
        scoreboard.left_paddle_point()
    if ball.xcor() + 20 < -(SCREEN_WIDTH / 2) - 10:
        # PLAYER 1 GETS A POINT
        ball.reset_position()
        scoreboard.right_paddle_point()
    # Detect ball collision with the paddles.
    if ball.xcor() > 340 and ball.distance(right_player) < 50 or ball.distance(left_player) < 50 and \
            ball.xcor() < -340:
        ball.bounce_x()

screen.exitonclick()
