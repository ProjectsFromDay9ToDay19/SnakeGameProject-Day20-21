import time
import turtle
from turtle import Screen, Turtle
from snake import Snake

# Setting up the screen
game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("Starving mamba")
game_screen.tracer(0)

snake = Snake()

game_screen.listen()
game_screen.onkey(fun=snake.up, key="Up")
game_screen.onkey(fun=snake.down, key="Down")
game_screen.onkey(fun=snake.left, key="Left")
game_screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(0.2)
    snake.move()

# keeping the screen on
game_screen.exitonclick()
