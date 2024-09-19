from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_cars = Turtle("square")
            new_cars.penup()
            new_cars.shapesize(stretch_wid=1, stretch_len=2)
            new_cars.color(random.choice(COLORS))
            new_cars.speed("fastest")
            random_x = 250
            random_y = random.randint(-200, 200)
            new_cars.goto(random_x, random_y)
            self.all_cars.append(new_cars)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def move_fast(self):
        self.car_speed += MOVE_INCREMENT





