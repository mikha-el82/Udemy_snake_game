from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")  # without animation
        rand_x = 20 * random.randint(-14, 14)
        rand_y = 20 * random.randint(-14, 14)
        self.goto(rand_x, rand_y)

    def refresh(self):
        rand_x = 20 * random.randint(-14, 14)
        rand_y = 20 * random.randint(-14, 14)
        self.goto(rand_x, rand_y)
