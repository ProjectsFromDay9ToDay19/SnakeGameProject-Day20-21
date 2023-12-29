import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh_position()

    def refresh_position(self):
        random_x = random.randrange(-280, 280, 20)
        random_y = random.randrange(-280, 280, 20)
        self.goto((random_x, random_y))
