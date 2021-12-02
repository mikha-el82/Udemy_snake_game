from turtle import Screen
from snake import Snake
from food import Food

import time

screen = Screen()
screen.setup(width=600, height=600)  # TODO #1 Include screen width in food to get random location
screen.bgcolor("black")
screen.title("Udemy Snake Game")
screen.tracer(0)  # sets turtle animation off

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# TODO #1 Remove colors of squares
# for testing - to differentiate between squares
snake.snake_segments[0].color("green")
snake.snake_segments[1].color("blue")

game_is_on = True
screen.update()

# moving of the rest of the snake
while game_is_on:
    time.sleep(0.5)
    snake.move()
    screen.update()
    # game_is_on = False

    if snake.head.distance(food) < 10:
        print("nom nom nom")
        food.refresh()

screen.exitonclick()
