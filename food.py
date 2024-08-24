from turtle import Turtle
import random
COLOR_FOOD = ["yellow","pink",'orange','violet','purple','red']
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.color("yellow")
        self.speed(0)
        self.refresh()
        
    def refresh(self):
        self.goto(20 * random.randint(0,15), 20 * random.randint(0,15))
        self.color(random.choice(COLOR_FOOD))


        