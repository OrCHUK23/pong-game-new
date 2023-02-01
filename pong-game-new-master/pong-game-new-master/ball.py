from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.x_move = random.choice(DIRECTIONS)
        # self.y_move = random.choice(DIRECTIONS)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    def move(self):
        """
        Function handles ball's constant movement.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Function handles change of ball direction when it hits the top or bottom wall.
        """
        self.y_move *= - 1

    def bounce_x(self):
        """
        Function handles change of ball direction when it hits the top or bottom wall.
        """
        self.x_move *= - 1
        self.move_speed *= 0.8

    def reset_position(self):
        """
        Function handles position of the ball when it hits one of the paddles - changes its direction to the opposite one.
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
