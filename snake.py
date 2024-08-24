from turtle import Turtle

MOVE_DIST = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_SPEED = "fast"


# STARTING_POSITIONS.append((-60,0))
# STARTING_POSITIONS.append((-80,0))
# STARTING_POSITIONS.append((-100,0))

class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_seg = Turtle(shape="square")  #
            new_seg.speed(SNAKE_SPEED)
            new_seg.penup()
            new_seg.goto(position)
            new_seg.color("light green")
            self.segments.append(new_seg)
        # self.segments[0].shape("arrow")

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[i - 1].xcor()
            y_pos = self.segments[i - 1].ycor()
            self.segments[i].goto(x_pos, y_pos)

        self.segments[0].forward(MOVE_DIST)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def increase_tail(self, tail_position_x, tail_position_y):
        new_seg = Turtle(shape="square")
        new_seg.speed(SNAKE_SPEED)
        new_seg.penup()
        new_seg.goto(tail_position_x, tail_position_y)
        new_seg.color("light green")
        self.segments.append(new_seg)
