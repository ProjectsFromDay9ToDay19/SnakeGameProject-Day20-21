import time
import turtle
from turtle import Screen, Turtle

# Setting up the screen
game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("Starving mamba")
game_screen.tracer(0)

# creating the snake body
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(0.2)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)

# keeping the screen on
game_screen.exitonclick()
