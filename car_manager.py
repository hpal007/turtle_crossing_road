from turtle import Turtle, colormode
import random

MOVE_INCREMENT = 10
START_MOVE_DISTANCE = 5
COLOR = ['red', 'medium violet red', 'lime', 'green', 'olive drab', 'dark cyan',
         'dark orange', 'dark red', 'yellow']


class CarManager:
    colormode(255)

    def __init__(self):
        self.all_cars = []
        self.car_speed = START_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOR))
            # new_car.setheading(180)
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(START_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT







