import turtle,time
from turtle import Screen, Turtle

game_screen = Screen()
game_screen.setup(width=600, height=600)
turtle.colormode(255)
game_screen.title("Snake🐍 Game")
# game_screen.bgcolor(255, 201, 0)
game_screen.bgcolor("black")
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
game_screen.tracer(0)
for pos in starting_positions:
    new_seg = Turtle()  #shape="square"
    new_seg.penup()
    new_seg.goto(pos)
    new_seg.color("white")
    new_seg.speed('slow')
    segments.append(new_seg)


while segments[0].xcor() != 280:
    game_screen.update()
    time.sleep(0.075)
    for segment in segments:
        segment.forward(20)








game_screen.exitonclick()