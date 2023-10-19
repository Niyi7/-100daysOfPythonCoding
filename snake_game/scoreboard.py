from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scores(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.ht()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align=ALIGNMENT,
            font=FONT,
        )

    def add_score(self):
        self.current_score += 1
        self.clear()
        self.update_scoreboard()
