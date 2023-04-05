from turtle import Screen
from Snake import Snake
import time
import random
# Static Variables
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

playing = True


while playing:
    screen.update()
    time.sleep(0.1)
    snake.movement()


screen.exitonclick()
