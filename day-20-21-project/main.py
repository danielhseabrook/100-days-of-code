from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from walls import Walls
# Static Variables
food = Food()
snake = Snake()
arena = Walls()
screen = Screen()
scoreboard = Scoreboard()
screen.setup(800, 800)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.title(f"My Snake Game")
score = 0
playing = True

while playing:
    if food.size >= snake.snakehead.distance(food) <= 15:
        food.move_food()
        score += 1
        scoreboard.scoreboard(score)
        snake.add_segment()
    playing = snake.check_health()
    time.sleep(0.1) 
    snake.movement()
    screen.update()
scoreboard.game_over()
screen.exitonclick()
