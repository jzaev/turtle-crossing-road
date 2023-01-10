from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.pu()
        self.goto(-200, 250)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.color("black")
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.color("white")

    def write_gameover(self):
        self.clear()
        self.color("black")
        self.goto(0, 0)
        self.write(f"G A M E    O V E R", align="center", font=FONT)
        self.color("white")
