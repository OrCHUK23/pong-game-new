from turtle import Turtle
import random
DIRECTIONS = [20, -20]  # Random directions for ball init.

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.x_move = random.choice(DIRECTIONS)
        # self.y_move = random.choice(DIRECTIONS)
        self.x_move = 20
        self.y_move = 20

    def move(self):
        """
        Function handles ball's constant movement.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        """
        Function handles change of ball direction when it hits the top or bottom wall.
        """
        self.y_move *= - 1
