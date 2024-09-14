# paddle.py
from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position, width):
        super().__init__()
        self.shape("square")
        self.color("orange")
        self.shapesize(stretch_wid=1, stretch_len=width)
        self.penup()
        self.goto(position)
        self.width = width

    def go_left(self):
        new_x = self.xcor() - 20
        if new_x > -360:  # Boundary check
            self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        if new_x < 360:  # Boundary check
            self.goto(new_x, self.ycor())

    def shrink(self):
        self.width *= 0.95
        self.shapesize(stretch_wid=1, stretch_len=self.width)
