import random
import turtle,time
from turtle import Screen, Turtle

game_screen = Screen()
game_screen.setup(width=800, height=800)
turtle.colormode(255)
game_screen.title("Snake🐍 Game")
game_screen.bgcolor(255, 201, 0)
game_screen.bgcolor("black")
game_screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
bait_list=[]
for pos in starting_positions:
    new_seg = Turtle(shape="square")
    new_seg.penup()
    new_seg.goto(pos)
    new_seg.color("white")
    segments.append(new_seg)


def direction_left():
    segments[0].left(90)


def direction_right():
    segments[0].right(90)


game_screen.listen()
game_screen.onkey(fun=direction_right, key="l")
game_screen.onkey(fun=direction_left, key="j")


is_game_on=True
while is_game_on:
    game_screen.update()
    time.sleep(0.25)
    for i in range(len(segments)-1,0,-1):
        x_pos=segments[i-1].xcor()
        y_pos=segments[i-1].ycor()
        segments[i].goto(x_pos,y_pos)
    segments[0].forward(20)


game_screen.exitonclick()
