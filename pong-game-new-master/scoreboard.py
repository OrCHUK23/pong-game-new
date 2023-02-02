from turtle import Turtle

ALIGNMENT = "center"
GAME_FONT = ("Courier", 80, "bold")
WIN_FONT = ("Courier", 30, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-120, 180)
        self.write(self.l_score, align=ALIGNMENT, font=GAME_FONT)
        self.goto(120, 180)
        self.write(self.r_score, align=ALIGNMENT, font=GAME_FONT)

    def right_player_win(self):
        self.goto(0, 0)
        self.color("turquoise")
        self.write(f"Right player is the Winner!", align=ALIGNMENT, font=WIN_FONT)

    def left_player_win(self):
        self.goto(0, 0)
        self.color("turquoise")
        self.write(f"Left player is the Winner!", align=ALIGNMENT, font=WIN_FONT)

    def left_paddle_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def right_paddle_point(self):
        self.r_score += 1
        self.update_scoreboard()
