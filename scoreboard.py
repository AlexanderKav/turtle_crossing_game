from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-150, 250)
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=FONT)


    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=FONT)

    def level_up(self):
        self.level = self.level + 1

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)

