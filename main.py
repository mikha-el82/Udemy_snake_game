from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Udemy Snake Game")
screen.tracer(0)  # sets turtle animation off

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
screen.update()

# moving of the rest of the snake
while game_is_on:
    time.sleep(0.2)
    snake.move()
    screen.update()

    # detect collision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.reset_scoreboard()
        snake.reset_snake()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
