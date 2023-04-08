from turtle import Turtle
from snake import Snake
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.size = 20
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(0.5, 0.5, 1)
        self.setposition(random.randint(-270, 270), random.randint(-270, 270))
        self.foodpos = self.pos()



    # def __init__(self):
    #     self.size = 20
    #     self.f_1 = Turtle(shape="circle")
    #     self.f_1.color("blue")
    #     self.f_1.penup()
    #     self.f_1.shapesize(0.5, 0.5, 1)
    #     self.f_1.setposition(random.randint(-270, 270), random.randint(-270, 270))
    #     self.foodpos = self.f_1.pos()
    #
    def move_food(self):
        self.setposition(random.randint(-270, 270), random.randint(-270, 270))
        self.foodpos = self.pos()



