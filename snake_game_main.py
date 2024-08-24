import snake,time
from turtle import Screen,colormode
from food import Food
from scoreboard import Scoreboard
from wall import Wall


game_screen = Screen()
game_screen.setup(width=800, height=800)
colormode(255)
game_screen.title("Snake🐍 Game")
# game_screen.bgcolor(255, 201, 0)
game_screen.bgcolor("black")

game_screen.tracer(0)


food=Food()
wall=Wall()
anaconda=snake.Snake()
scoreboard=Scoreboard()

game_screen.listen()
game_screen.onkey(key="Up",fun=anaconda.up)
game_screen.onkey(key="Down",fun=anaconda.down)
game_screen.onkey(key="Left",fun=anaconda.left)
game_screen.onkey(key="Right",fun=anaconda.right)

game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(0.1)
    anaconda.move()
    if anaconda.segments[0].distance(food) < 11 :
        food.refresh()
        anaconda.increase_tail(tail_position_x=food.xcor(),tail_position_y=food.ycor())
        scoreboard.clear()
        scoreboard.update_score()

    # detect collision with wall
    if anaconda.segments[0].xcor() <= -330 or anaconda.segments[0].ycor() >= 330 or anaconda.segments[0].xcor() >= 318 or anaconda.segments[0].ycor() <= -320 :
        game_is_on = False
        scoreboard.game_over()
        food.goto(909, 909)
        game_screen.update()
        time.sleep(0.1)
        temp = True
        while temp:
            anaconda.move()
            if anaconda.segments[0].xcor() > 500:
                temp = False
            if anaconda.segments[0].ycor() > 500:
                temp = False
        game_screen.update()
        time.sleep(0.1)



    #detect collision with its own tail
    for seg in anaconda.segments[2:]:
        if anaconda.segments[0].distance(seg) <= 5 :
            seg.color("red")
            game_screen.update()
            game_is_on = False
            scoreboard.game_over()
            food.goto(909, 909)

game_screen.exitonclick()