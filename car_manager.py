from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 6:
            turtle = Turtle()
            turtle.penup()
            turtle.shapesize(1, 2)
            turtle.shape("square")
            turtle.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            turtle.goto(300, random_y)
            self.all_cars.append(turtle)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
