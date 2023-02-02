from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from net import Net

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
REQUIRED_POINTS = 3  # Required points to win the game.
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
# Create the two players and place them at the left and right edges of the screen.
right_player = Paddle(screen_width=SCREEN_WIDTH / 2 - 30, screen_height=SCREEN_HEIGHT)
left_player = Paddle(screen_width=-SCREEN_WIDTH / 2 + 30, screen_height=SCREEN_HEIGHT)
ball = Ball()  # Creating the ball.
scoreboard = Scoreboard()  # Creating the scoreboard to track the points.
net = Net()  # Creating the middle net

# Create screen listening to up and down movements.
screen.onkeypress(right_player.go_up, "Up")
screen.onkeypress(right_player.go_down, "Down")
screen.onkeypress(left_player.go_up, "w")
screen.onkeypress(left_player.go_down, "s")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # Updates the screen manually because screen.tracer is off.
    ball.move()  # Start constant movement of the ball.
    # Detect ball collision with top and bottom walls.
    if ball.ycor() > (SCREEN_HEIGHT / 2) - 20 or ball.ycor() < -(SCREEN_HEIGHT / 2) + 30:
        ball.bounce_y()
    # Handle ball is out of left and right walls.
    if ball.xcor() + 20 < -(SCREEN_WIDTH / 2) - 10:
        # PLAYER 1 GETS A POINT
        ball.reset_position()
        scoreboard.right_paddle_point()
    if ball.xcor() > (SCREEN_WIDTH / 2):
        # PLAYER 2 GETS A POINT
        ball.reset_position()
        scoreboard.left_paddle_point()
    # Detect ball success collision with one of the paddles.
    if ball.xcor() > 340 and ball.distance(right_player) < 50 or ball.distance(left_player) < 50 and \
            ball.xcor() < -340:
        ball.bounce_x()
    # Win checking.
    if scoreboard.r_score == REQUIRED_POINTS:
        game_is_on = False
        scoreboard.right_player_win()
    elif scoreboard.l_score == REQUIRED_POINTS:
        game_is_on = False
        scoreboard.left_player_win()
screen.exitonclick()
