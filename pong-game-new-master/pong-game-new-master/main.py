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
screen.title("My Pong Game2")
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
    screen.update()  # Updates the screen manually because screen.tracer is off (0)
    ball.move()
    # Detect ball collision with top and bottom walls.
    if ball.ycor() > (SCREEN_HEIGHT / 2) - 20 or ball.ycor() < -(SCREEN_HEIGHT/2) + 30:
        ball.bounce()
    # Handle ball is out of left and right walls.
    if ball.xcor() > (SCREEN_WIDTH/2):
        # PLAYER 2 GETS A POINT
        ball = Ball()
    if ball.xcor() + 20 < -(SCREEN_WIDTH/2) - 10:
        # PLAYER 1 GETS A POINT
        ball = Ball()
    # Detect ball collision with the paddles.
    if ball.distance(right_player) < 10:
        # print("YES")
        ball.setx(ball.xcor() * -1)
    if ball.xcor() == 1:
        pass
screen.exitonclick()
