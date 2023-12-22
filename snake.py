from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.snake_body.append(new_segment)

    def move(self):
        for segment_index in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment_index - 1].xcor()
            new_y = self.snake_body[segment_index - 1].ycor()
            self.snake_body[segment_index].goto(new_x, new_y)

        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)
