from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __int__(self):
        self.segments = []
        self.game_start()

    def game_start(self):
        for n in STARTING_POSITIONS:
            t_n = Turtle("square")
            t_n.penup()
            t_n.color("white")
            t_n.goto(n)
            self.segments.append(t_n)

    def movement(self):
        for n in range(len(self.segments) - 1, 0, -1):
            snake_position = self.segments[n - 1].position()
            self.segments[n].goto(snake_position)
        self.segments[0].forward(MOVE_DISTANCE)




