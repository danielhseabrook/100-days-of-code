from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.game_start()
        self.snakehead = self.segments[0]
        self.size = 40

    def game_start(self):
        for n in range(0, len(STARTING_POSITIONS)):
            t_n = Turtle("square")
            t_n.penup()
            t_n.color("white")
            t_n.goto(STARTING_POSITIONS[n])
            self.segments.append(t_n)

    def movement(self):
        for n in range(len(self.segments) - 1, 0, -1):
            snake_position = self.segments[n - 1].position()
            self.segments[n].goto(snake_position)
        self.snakehead.forward(MOVE_DISTANCE)

    def add_segment(self):
        t_name = Turtle("square")
        t_name.penup()
        t_name.color("white")
        self.segments.append(t_name)

    def check_health(self):
        if self.snakehead.xcor() <= -300 or self.snakehead.xcor() >= 300 or self.snakehead.ycor() <= -300 or \
        self.snakehead.ycor() >= 300:
            return False

        for n in self.segments[1:]:
            if self.snakehead.distance(n) < 10:
                return False
            else:
                return True
        return True

    def up(self):
        if self.snakehead.heading() == 270:
            pass
        else:
            self.snakehead.seth(90)

    def down(self):
        if self.snakehead.heading() == 90:
            pass
        else:
            self.snakehead.seth(270)

    def left(self):
        if self.snakehead.heading() == 0:
            pass
        else:
            self.snakehead.seth(180)

    def right(self):
        if self.snakehead.heading() == 180:
            pass
        else:
            self.snakehead.seth(0)


