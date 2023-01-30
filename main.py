from turtle import Screen, Turtle
import time

from ball import Ball
# from scoreboard import Scoreboard
from paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
# Create the two players and place them at the left and right edges of the screen.
right_player = Paddle(screen_width=SCREEN_WIDTH / 2 - 30, screen_height=SCREEN_HEIGHT)
left_player = Paddle(screen_width=-SCREEN_WIDTH / 2 + 30, screen_height=SCREEN_HEIGHT)
ball = Ball()

# Create screen listening to up and down movements.
screen.listen()
screen.onkey(right_player.go_up, "Up")
screen.onkey(right_player.go_down, "Down")
screen.onkey(left_player.go_up, "w")
screen.onkey(left_player.go_down, "s")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()  # Function that updates the screen manually because screen.tracer is off (0)
    ball.move(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)
screen.exitonclick()

