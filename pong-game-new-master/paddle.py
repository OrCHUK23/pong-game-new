from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Paddle(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(screen_width, 0)
        self.speed("fastest")
        self.__screen_width = screen_width
        self.__screen_height = screen_height

    def go_up(self):
        """
        Function handles the up movement of one of the paddles.
        """
        new_y = self.ycor() + 30
        if self.__check_top_wall(self.__screen_height):
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Function handles the down movement of one of the paddles.
        """
        new_y = self.ycor() - 30
        if self.__check_bottom_wall(self.__screen_height):
            self.goto(self.xcor(), new_y)

    def __check_top_wall(self, screen_height):
        """
        Private function that detects paddle collision with the top wall.
        :param screen_height: Height of the screen
        """
        return self.ycor() < (screen_height / 2) - 50

    def __check_bottom_wall(self, screen_height):
        """
        Private function that detects paddle collision with the bottom wall.
        :param screen_height: Height of the screen
        """
        return self.ycor() > ((screen_height / 2) * - 1) + 60
