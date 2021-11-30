from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Udemy Snake Game")
screen.tracer(0)

# TODO #1: Create snake body
snake_segments = []
for i in range(3):  # initial length of the snake
    snake_segments.append(Turtle(shape="square"))
    snake_segments[i].color("white")
    snake_segments[i].penup()
    x_pos = i * -20
    y_pos = 0
    snake_segments[i].goto(x=x_pos, y=y_pos)
screen.update()


# TODO #2: Move snake
# for testing - to differentiate between squares
snake_segments[0].color("green")
snake_segments[1].color("blue")

game_is_on = True
screen.update()

# moving of the rest of the snake
while game_is_on:
    for i in range(len(snake_segments) - 1, 0, -1):
        snake_segments[i].goto(snake_segments[i - 1].pos())
    #  snake[0].left(30)
    snake_segments[0].forward(20)
    time.sleep(1)
    screen.update()
    # game_is_on = False

screen.exitonclick()
