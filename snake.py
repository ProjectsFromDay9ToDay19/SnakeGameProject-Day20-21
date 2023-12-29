from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for segment_index in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment_index - 1].xcor()
            new_y = self.snake_body[segment_index - 1].ycor()
            self.snake_body[segment_index].goto(new_x, new_y)

        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segment in self.snake_body:
            segment.goto(1500, 1500)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    """def increase_speed(self):
        # self.speed += 5
        for segment in self.segments:
            segment.speed(self.speed)"""

    """def print_current_speed(self):
        self.segments[0].goto(x=-590, y=350)
        self.clear()
        self.write(arg=f"Current Speed : {self.speed}", align=ALIGNMENT, font=FONT)
"""