import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
screen.listen()
screen.onkey(player.move, 'Up')
score=Scoreboard()
list_of_cars=[]
game_is_on = True
while game_is_on:
    time.sleep(0.01)

    num = random.randint(1, 50)
    if num == 1:
        new_car = CarManager()
        list_of_cars.append(new_car)

        for car in list_of_cars:
            car.move()

     #checking collision

    for car in list_of_cars:
        if car.distance(player) < 30:

            score.game_over()
            time.sleep(2)
            game_is_on = False

    # level up

    if player.ycor() >= 280:
        score.update_score()
        car.level_up()
        player.starting_position()
        car.level_up()




    screen.update()


