from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 360)
        
        self.high_score = 0
        self.score = 0
        self.write(f"Score : {self.score}", move=False, align="center",font=('Courier', 20, 'bold'))

    def update_score(self): 
        self.score += 1
        self.score_color()
        self.goto(0, 360)
        self.write(f"Score : {self.score}", move=False, align="center",font=('Courier', 20, 'bold'))

    def game_over(self):
        print("gsgbsj")
        self.goto(-10, 10)
        self.color("red")
        self.write(f"GAME OVER", move=False, align="center", font=('Courier', 35, 'bold'))
        self.goto(-10, -20)
        self.score_color()
        self.write(f"Final Score : {self.score}", move=False, align="center", font=('Courier', 25, 'bold'))
        self.score = 0
        if self.score > self.high_score:
            self.high_score = self.score


    def score_color(self):
        if self.score > 30:
            self.color("green")
        elif self.score > 20:
            self.color("yellow")
        elif self.score > 5:
            self.color("blue")
        else:
            self.color("red")

    def keep_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.goto(300, 360)
        self.color("orange")
        self.write(f"Highest : {self.high_score}", move=True, align="Right", font=('Courier', 20, 'bold'))
        self.goto(0, 360)
