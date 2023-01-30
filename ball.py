from turtle import Turtle


MOVE_DISTANCE = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.8)

    def move(self, screen_width, screen_height):
        step = 20
        dx = self.xcor() + step
        dy = self.ycor() + step

        self.goto(dx, dy)

    def __check_top_wall(self, screen_height):
        if self.ycor() < (screen_height / 2) - 50:
            return True
        return False

    def __check_bottom_wall(self, screen_height):
        if self.ycor() > ((screen_height / 2) * - 1) + 60:
            return True
        return False