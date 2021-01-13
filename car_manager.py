from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0


class CarManager(Turtle):
    def __init__(self):
        super().__init__()

        self.generate_car()

    def generate_car(self):

        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(280, random.randint(-250, 250))
        self.setheading(180)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT)

    def level_up(self):
        global MOVE_INCREMENT
        MOVE_INCREMENT = MOVE_INCREMENT + 10





