import time
import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WIDTH = 1200
HEIGHT = 720
SLEEP_TIME = 1

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Mamba Snake Game")
screen.tracer(0)

snake = Snake()
ball = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
sleep_time = SLEEP_TIME / 10
while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    snake.move()

    # Detect collision with food
    if snake.head.distance(ball) < 15:
        ball.refresh_position()
        snake.extend()
        scoreboard.increase_score()
        
    if scoreboard.score > 1 and scoreboard.score % 5 == 0:
        sleep_time *= 0.999

    # Detect collision with wall.
    head = snake.head
    has_hit_wall = not -(WIDTH/2) + 15 < head.xcor() < WIDTH/2 - 15 or not (-HEIGHT / 2) + 15 < head.ycor() < HEIGHT/2 - 15
    if has_hit_wall:
        scoreboard.reset()
        snake.reset()
        sleep_time = SLEEP_TIME / 10

    # Detect collision with its own tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) <= 10:
            game_is_on = False
            scoreboard.game_over()


# keeping the screen on
screen.exitonclick()
