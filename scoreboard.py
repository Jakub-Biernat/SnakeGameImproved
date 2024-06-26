from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.write_score()

    def restart_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.write_score()
