from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 300)

    def scoreboard(self, score):
        self.clear()
        current_score = 0
        current_score += score
        self.write(f"Score {current_score}", move=False, align='center', font=('Arial', 12, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align='center', font=('Arial', 20, 'normal'))

