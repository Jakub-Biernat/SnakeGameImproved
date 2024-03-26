from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed(0)
        self.goto(randint(-285, 285), randint(-285, 285))

    def refresh(self):
        self.goto(randint(-285, 285), randint(-285, 285))
