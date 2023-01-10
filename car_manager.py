import random
from turtle import Turtle
from random import choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.turns = 0

    def move(self):
        for car in self.cars:
            car.goto(car.xcor()-MOVE_INCREMENT, car.ycor())

    def remove_used_cars(self):
        pass
        # for car in self.cars:
        #     if car.xcor() < -350:
        #         del self.cars.pop(car.)

    def add_car(self):
        if self.turns % STARTING_MOVE_DISTANCE != 0:
            return
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(COLORS))
        new_car.pu()
        y = random.randint(100, 500)
        new_car.goto(300 - STARTING_MOVE_DISTANCE, y - 250)
        self.cars.append(new_car)

    def check_crash(self, turtle_pos):
        for car in self.cars:
            if car.distance(turtle_pos) < 20:
                return True
        return False

    def turn_ok(self, turtle_pos):
        self.move()
        self.add_car()
        self.remove_used_cars()
        self.turns += 1
        return not self.check_crash(turtle_pos)
