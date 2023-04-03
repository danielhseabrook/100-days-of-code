from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(500, 400)
turtle_colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", ]
turtle_list = []
count = 0
y = 0
racing = True
for colour in turtle_colours:
    x = -225
    count += 1
    y = 210 + (count * -50)
    t_colour = Turtle()
    t_colour.shape("turtle")
    t_colour.color(colour)
    t_colour.penup()
    t_colour.goto(-225, y)
    # colour_position = t_colour.xcor()
    turtle_list.append(t_colour)


# User bet #
user_bet = screen.textinput("Turtle Race Course", "Please enter the colour of the turtle you wish to bet on.").lower


while racing:
    for racer in turtle_list:
        if racer.xcor() > 225.00:
            winner = racer.color()
            winner_colour = winner[1]
            if winner == user_bet:
                print(f"Your turtle won. The winning colour was {winner_colour}!")
            else:
                print(f"Your turtle lost. The winning colour was {winner_colour}!")
            racing = False
        else:
            speed = random.randint(1, 10)
            racer.forward(speed)


screen.exitonclick()









