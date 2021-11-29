from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Udemy Snake Game")
screen.tracer(0)

# TODO #1: Create snake body
snake = []
for i in range(3):
    snake.append(Turtle(shape="square"))
    snake[i].color("white")
    snake[i].penup()
    x_pos = i * -20
    y_pos = 0
    snake[i].goto(x=x_pos, y=y_pos)
screen.update()

# TODO #2: Move snake
game_is_on = True
while game_is_on:
    for segment in snake:
        segment.forward(20)
    time.sleep(0.5)
    screen.update()

screen.exitonclick()
