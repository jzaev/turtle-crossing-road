import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

tim = Player()
car_manager = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(tim.go, "Up")
board = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if not car_manager.turn_ok(tim.pos()):
        board.write_gameover()
        game_is_on = False

    if tim.i_win():
        board.score += 1
        board.write_score()
        tim.to_start()

screen.exitonclick()
