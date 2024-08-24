from turtle import Turtle,Screen
import time 
VAL=20
class Wall:
    def __init__(self):
        self.wall=Turtle()
        self.wall.speed(0)
        self.wall.hideturtle()
        self.wall.penup()
        self.wall.goto(310,-310)
        self.wall.pendown()
        self.draw_wall()
        


    def draw_wall(self):
        for l in range (0,4):

            for i in range(0,32):
                self.colorchange(i)
                self.wall.begin_fill()
                self.square()
                self.wall.end_fill()
                self.wall.backward(VAL)
            self.wall.right(90)

    
    def square(self):
        for i in range(0,4):
            self.wall.right(90)
            self.wall.forward(VAL)

    def colorchange(self,j):
        if j % 2 == 0:
            self.wall.color("light grey")
        else:
            self.wall.color("grey")


        
