from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.to_start()

    def go(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def i_win(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def to_start(self):
        self.goto(STARTING_POSITION)
