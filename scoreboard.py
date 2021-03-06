from turtle import Turtle

ALIGNMENT = 'center'
FONT_L = ("Courier", 14, "normal")
FONT_G = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.goto(-220, 260)
        self.color("black")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Level: {self.level} ', align=ALIGNMENT, font=FONT_L)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER !!! ', align=ALIGNMENT, font=FONT_G,)
