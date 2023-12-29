import time
import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Setting up the screen
game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("Starving mamba")
game_screen.tracer(0)

snake = Snake()
ball = Food()
scoreboard = Scoreboard()

game_screen.listen()
game_screen.onkey(fun=snake.up, key="Up")
game_screen.onkey(fun=snake.down, key="Down")
game_screen.onkey(fun=snake.left, key="Left")
game_screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(ball) < 15:
        ball.refresh_position()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if not -280 <= snake.head.xcor() <= 280 or (not -290 <= snake.head.ycor() <= 290):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with its own tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) <= 10:
            game_is_on = False
            scoreboard.game_over()


# keeping the screen on
game_screen.exitonclick()
