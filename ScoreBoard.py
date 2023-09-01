from turtle import Turtle

FONT_NAME = "Courier"
FONT_SIZE = 50
FONT_TYPE = "bold"
ALIGN_SCOREBOARD = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 220)
        self.score_keeper()

    def left_scored(self):
        self.left_score += 1
        self.score_keeper()

    def right_scored(self):
        self.right_score += 1
        self.score_keeper()

    def score_keeper(self):
        self.clear()
        self.write(f"{self.left_score}  {self.right_score}", False, ALIGN_SCOREBOARD, (FONT_NAME, FONT_SIZE, FONT_TYPE))

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game  Over", False, ALIGN_SCOREBOARD, (FONT_NAME, FONT_SIZE, FONT_TYPE))
