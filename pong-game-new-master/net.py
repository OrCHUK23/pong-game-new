from turtle import Turtle

STARTING_POSITIONS = [
    (0, -250),
    (0, -150),
    (0, -50),
    (0, 50),
    (0, 150),
    (0, 250),
]  # Positions for the net squares.


class Net(Turtle):
    def __init__(self):
        self.net = []
        self.create_net()

    def create_net(self):
        """
        Function handles the creation of the net squares.
        """
        for position in STARTING_POSITIONS:
            net_segment = Turtle("square")
            net_segment.color("white")
            net_segment.penup()
            net_segment.shapesize(stretch_wid=3, stretch_len=0.6)
            net_segment.goto(position)
            net_segment.speed("fastest")
            self.net.append(net_segment)
