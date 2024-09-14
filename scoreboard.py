# scoreboard.py
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.current_score = 0
        self.high_score = 0
        self.lives = 3  # Start with 3 lives
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # Display current score on the left
        self.goto(-200, 270)
        self.write(f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)
        # Display high score on the right
        self.goto(200, 270)
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        # Display lives at the top center
        self.goto(0, 270)
        self.write(f"Lives: {self.lives}", align=ALIGNMENT, font=FONT)

    def add_score(self, points):
        self.current_score += points
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.current_score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
