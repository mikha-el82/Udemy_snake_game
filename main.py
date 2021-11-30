from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Udemy Snake Game")
screen.tracer(0) # sets turtle animation off

snake = Snake()
screen.update()

# TODO #1 Remove colors of squares
# for testing - to differentiate between squares
snake.snake_segments[0].color("green")
snake.snake_segments[1].color("blue")

game_is_on = True
screen.update()

# moving of the rest of the snake
while game_is_on:
    snake.move()
    time.sleep(1)
    screen.update()
    # game_is_on = False

screen.exitonclick()
