from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:  # initial length of the snake
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.snake_segments.append(new_segment)

    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[i].goto(self.snake_segments[i - 1].pos())
        #  snake[0].left(30)
        self.snake_segments[0].forward(MOVE_DISTANCE)
