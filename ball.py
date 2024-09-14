# ball.py
from turtle import Turtle

# Constants
BALL_INITIAL_SPEED = 0.05

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_wid=1, stretch_len=1)  # Ensures the ball stays a consistent size
        self.penup()
        self.speed = BALL_INITIAL_SPEED
        self.x_move = 10
        self.y_move = 10
        self.move_speed = BALL_INITIAL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def move_small_step(self, steps):
        # Break ball movement into smaller steps for smoother animation
        new_x = self.xcor() + self.x_move / steps
        new_y = self.ycor() + self.y_move / steps
        self.goto(new_x, new_y)

    def bounce_off_y_vertical_walls(self):
        self.y_move *= -1

    def bounce_off_x_walls(self):
        self.x_move *= -1

    def bounce_off_paddle(self):
        self.y_move *= -1  # Reverse the vertical direction when it hits the paddle

    def reset_position(self):
        self.goto(0, -200)  # Reset to the middle of the screen near the bottom
        self.x_move = 10  # Reset x-axis movement
        self.y_move = 10  # Ensure it moves upwards by setting y_move positive
        self.move_speed = BALL_INITIAL_SPEED
